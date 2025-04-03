from streamlit.runtime.state import SessionStateProxy
import threading
import datetime
from Scrapper.PrimerLeague import PremierLeagueCrawler
from Scrapper.scrapperData import Data as scrapperData
import RAG.Data as RAG_Data
from RAG.RAG_app import RAG_application
from langchain_openai import ChatOpenAI
import os
update_interval = 1 * 1 * 10 # 24 hours (hr * min * sec)

# ToDo: 1. Logging System

def system_init(llm: ChatOpenAI):
    """
    Initialize the project variables.
    """   
    # Update RAG Vector Store
    if check_RAG_vector_db_exist():
        add_doc_to_RAG_vector_db()
    else:
        create_RAG_vector_db()
        add_doc_to_RAG_vector_db()

def update_PremierLeague_data(llm: ChatOpenAI):
    """
    Update the Premier League data from fbref.com.
    """
    try:
        crawler = PremierLeagueCrawler()

        # Get all teams url
        # crawler.getTeamsUrl()
        
        # Scrap & Save data
        #for team_name, team_url in crawler.teamsInfo.items():
        #    team_data = crawler.scrap(team_url)
        #    crawler.preprocess_data(team_data)
        #    crawler.save_data(team_data, team_name, output_dir=scrapperData.team_data_savePath, 
        #                      save_as_excel=True)

        # Transform data to md file
        #md_threads = []
        #i = 0
        #for team_name in crawler.teamsInfo.keys():
        #    thread = threading.Thread(target=transfrom_team_data_to_md, args=(scrapperData.team_data_savePath , team_name, llm))
        #    md_threads.append(thread)
        #    if i == 2:
        #        break
        #    i += 1

        #for thread in md_threads:
        #    thread.start()

    except Exception as e:
        pass

def transfrom_team_data_to_md(filePath: str, team_name: str, llm: ChatOpenAI):
    """
    Transform the team data to md file.
    """
    team_stats_prompt = PremierLeagueCrawler.process_teamData_to_prompt(filePath + f"{team_name}_stats.xlsx", team_name)
    team_stats_md = PremierLeagueCrawler.transform_xlsx_to_md(team_stats_prompt, llm)
    PremierLeagueCrawler.save_md_to_file(team_stats_md, team_name)

def create_RAG_vector_db():
    """
    Create the RAG vector store.
    """
    Rag_app = RAG_application()
    Rag_app.create_vector_db()

def add_doc_to_RAG_vector_db():
    """
    Update the RAG vector store.
    """
    Rag_app = RAG_application()
    crawler = PremierLeagueCrawler()
    crawler.getTeamsUrl()
    try:
        for team_name in PremierLeagueCrawler.teamsInfo.keys():
            team_data = PremierLeagueCrawler.load_md_as_str(
                f"{scrapperData.team_data_savePath}{team_name}_all_stats.md")
            docs = Rag_app.split_documents(team_data)
            Rag_app.add_doc_to_vector_db(docs)
    except Exception as e:
        print(f"Error: {e}")

def check_RAG_vector_db_exist() -> bool:
    """
    Check if the vector db exists.
    """
    if not os.path.exists(RAG_Data.persist_directory):
        return False
    else:
        return True

def setup_scheduled_updates(**session_state: SessionStateProxy):
    """
    Setup the scheduled updates for the Premier League data.
    """
    # Check if the update thread is already running
    if "update_thread" not in session_state or not session_state["update_thread"].is_alive():
        session_state["update_stop_event"] = threading.Event()
        session_state["update_thread"] = threading.Thread(
            target=_private_scheduled_update_worker,
            args=(session_state["update_stop_event"], session_state["LLM"])
        )
        session_state["update_thread"].daemon = True
        session_state["update_thread"].start()
    
    # Track last update time
    if "last_update_time" not in session_state:
        session_state["last_update_time"] = datetime.datetime.now()

def _private_scheduled_update_worker(stop_event: threading.Event, llm: ChatOpenAI):
    """
    Private worker for the scheduled updates.
    """
    while not stop_event.is_set():
        # Wait for next update
        stop_event.wait(update_interval)

        update_PremierLeague_data(llm)

def stop_scheduled_updates(**session_state: SessionStateProxy):
    """
    Stop the scheduled updates.
    """
    if "update_stop_event" in session_state:
        session_state.update_stop_event.set()
        session_state.update_thread.join(timeout=1)

def get_initial_graph_state():
    """
    Get the initial state for the graph state.
    """
    return {
    "user_query": "",
    "user_query_history": [],
    "response": "",
    "llm_transcript": "",

    # Flags
    "is_strategist_needed": False
}

