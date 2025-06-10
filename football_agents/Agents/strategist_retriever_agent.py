from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import Chroma
from RAG import Data as RAG_data
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from GraphState.strategist_state import StrategistState
from langchain_core.output_parsers import PydanticOutputParser
from Prompt import retrieve_template, interpret_query_prompt

def Retrieve_docs_for_strategist(llm, vector_db_name: str, state: StrategistState):
    """Retrieve and process documents for the strategist agent."""
    
    # Initialize vector store
    vector_store = Chroma(
        persist_directory=RAG_data.persist_directory,
        embedding_function=HuggingFaceEmbeddings(model_name=RAG_data.embedding_model),
        collection_name=vector_db_name
    )

    # Initialize interpret chain
    interpret_prompt = ChatPromptTemplate.from_messages(interpret_query_prompt)
    interpret_chain = interpret_prompt | llm | StrOutputParser()

    # Get documents based on state
    if state.can_doc_answer_question == False:
        docs = retrieve_docs(vector_store, state.rewritten_query)
        current_rewritten_query = state.rewritten_query
    else:
        current_rewritten_query = interpret_chain.invoke(state.user_query)
        docs = retrieve_docs(vector_store, current_rewritten_query)

    # Process documents with LLM
    prompt = ChatPromptTemplate.from_messages(retrieve_template)
    parser = PydanticOutputParser(pydantic_object=StrategistState)
    chain = (
        {"teams_data": RunnablePassthrough(), "user_query": RunnablePassthrough()}
        | prompt.partial(format_instructions=parser.get_format_instructions())
        | llm
        | parser
    )
    result = chain.invoke({"teams_data": docs["teams_data"], "user_query": state.user_query})

    # Convert documents to string format
    docs_str = "\n\n".join([doc.page_content for doc in docs["teams_data"]])

    return {
        "user_query": state.user_query,
        "documents": docs_str,  # Return documents as a string
        "rewritten_query": current_rewritten_query,
        "can_doc_answer_question": result.can_doc_answer_question
    }

def retrieve_docs(vector_store, retrieval_query):
    """Helper function to retrieve documents from vector store."""
    docs = vector_store.as_retriever(k=RAG_data.retrieval_k).invoke(retrieval_query)
    return {"teams_data": docs}
