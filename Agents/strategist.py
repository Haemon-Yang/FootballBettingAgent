from .state import GraphState
from .prompts import strategist_template
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import Chroma
from RAG import Data as RAG_data
from langchain_huggingface import HuggingFaceEmbeddings

class Strategist():
    def __init__(self, llm, vector_db_name: str):
        vector_store = Chroma(
            persist_directory=RAG_data.persist_directory,
            embedding_function=HuggingFaceEmbeddings(model_name=RAG_data.embedding_model),
            collection_name = vector_db_name
        )
        
        prompt = ChatPromptTemplate.from_messages(strategist_template)
        parser = StrOutputParser()
        chain = (
            {"context": vector_store.as_retriever(), "user_query": RunnablePassthrough()}
            | prompt
            | llm
            | parser
        )
        self.chain = chain