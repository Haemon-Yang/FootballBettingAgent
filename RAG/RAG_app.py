from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from typing import List
from Scrapper.PrimerLeague import PremierLeagueCrawler
import Data

class RAG_application:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name=Data.embedding_model)
        self.persist_directory = Data.persist_directory

        pass

    def split_documents(self,filePath: str) -> List[Document]:
        """
        Split documents into chunks.
        """
        team_data = PremierLeagueCrawler.load_md_as_str(filePath)

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
    
    def create_vector_store(self, docs: List[Document], collection_name: str) -> Chroma:
        """
        Create vector store for RAG.
        """
        try:
            db = Chroma.from_documents(
                documents=docs,
                embedding=self.embedding_model,
                persist_directory=self.persist_directory,
                collection_name=collection_name
            )
            db.persist()
        except Exception as e:
            print(f"Error creating vector store: {e}")
            return None
    
    