from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
import asyncio
from typing import List, Dict, Union, Any
from ..GraphState.deep_research_state import SearchQuery
import tiktoken
from ..GraphState.deep_research_state import SectionState
from dotenv import load_dotenv
from ..Data import NUMBER_OF_RESULTS

load_dotenv()
tavily_search = TavilySearchAPIWrapper()

async def search_web(state: SectionState):
    """ Search the web for each query, then return a list of raw sources and a formatted string of sources."""

    # Get state
    search_queries = state["search_queries"]
    print('--- Searching Web for Queries ---')
    # Web search
    query_list = [query.search_query for query in search_queries]
    search_docs = await run_search_queries(search_queries, num_results=NUMBER_OF_RESULTS, include_raw_content=True)
    # Deduplicate and format sources
    search_context = format_search_results(search_docs, max_tokens=4000, include_raw_content=True)

    print('--- Searching Web for Queries Completed ---')
    return {"source_str": search_context}

async def run_search_queries(
        search_queries: List[Union[str, SearchQuery]],
        num_results: int = 5,
        include_raw_content: bool = False,
)-> List[Dict]:
    search_tasks = []
    for query in search_queries:
        if isinstance(query, SearchQuery):
            query_str = query.search_query
        else:
            query_str = str(query)
    
        try:
            search_tasks.append(tavily_search.raw_results_async(
                query = query_str,
                max_results=num_results,
                search_depth='advanced',
                include_answer=False,
                include_raw_content=include_raw_content))
        except Exception as e:
            print(f"Error searching for {query_str}: {e}")
            continue
    
    if not search_tasks:
        return []
    else:
        try:
            search_docs = await asyncio.gather(*search_tasks, return_exceptions=True)
            valid_results = [
                doc for doc in search_docs if not isinstance(doc, Exception)
            ]
            return valid_results
        except Exception as e:
            print(f"Error in search_fromWeb: {e}")
            return []

def format_search_results(search_response: Union[Dict[str, Any], List[Any]],
                          max_tokens: int = 2000,
                          include_raw_content: bool = False) -> str:
    encoding = tiktoken.encoding_for_model('gpt-4o')
    source_list = []

    if isinstance(search_response, dict):
        if 'results' in search_response:
            source_list.extend(search_response['results'])
        else:
            source_list.append(search_response)
    elif isinstance(search_response, list):
        for response in search_response:
            if isinstance(response, dict):
                if 'results' in response:
                    source_list.extend(response['results'])
                else:
                    source_list.append(response)
            elif isinstance(response, list):
                source_list.extend(response)
    
    if not source_list:
        return "No search results found."
    
    # Save web url
    unique_sources = {}
    for source in source_list:
        if isinstance(source, dict) and 'url' in source:
            if source['url'] not in unique_sources:
                unique_sources[source['url']] = source

    # Format Output
    formatted_text = "Content from web search:\n\n"
    for i, source in enumerate(unique_sources.values(), 1):
        formatted_text += f"Source {source.get('title', 'Untitled')}:\n===\n"
        formatted_text += f"URL: {source['url']}\n===\n"
        formatted_text += f"Most relevant content from source: {source.get('content', 'No content available')}\n===\n"

        if include_raw_content:
            # Truncate raw webpage content
            raw_content = source.get("raw_content", "")
            if raw_content:
                tokens = encoding.encode(raw_content)
                truncated_tokens = tokens[:max_tokens]
                truncated_content = encoding.decode(truncated_tokens)
                formatted_text += f"Raw Content: {truncated_content}\n\n"

    return formatted_text.strip()
