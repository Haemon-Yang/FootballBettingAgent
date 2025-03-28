from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from typing import List
from . import Data

class RAG_application:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name=Data.embedding_model)
        self.persist_directory = Data.persist_directory
        self.db_collection_name = Data.db_collection_name_premier_league

    def split_documents(self, team_data: str) -> List[Document]:
        """
        Split documents into chunks.
        """
        headers_to_split_on = [
            ("###", "header_1"),
            ("##", "header_2"),
            ("#", "header_3"),
        ]
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
        md_header_splits = markdown_splitter.split_text(team_data)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", " ", ""],
            keep_separator=True
        )
        docs = text_splitter.split_documents(md_header_splits)
        return docs
    
    def create_vector_db(self):
        """
        Create vector store for RAG.
        """
        db = Chroma(
            collection_name=self.db_collection_name,
            embedding_function=self.embedding_model,
            persist_directory=self.persist_directory
        )

    def update_vector_store(self, docs: List[Document], ids: List[str]):
        """
        Update vector store for RAG.
        """
        try:
            db = Chroma(
                collection_name=self.db_collection_name,
                embedding_function=self.embedding_model,
                persist_directory=self.persist_directory
            )
            
            db.update_documents(
                documents=docs,
                ids=ids
            )
            db.persist()
        except Exception as e:
            print(f"Error creating vector store: {e}") 