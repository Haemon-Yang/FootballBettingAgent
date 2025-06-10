from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from typing import List
from . import Data
import re

class RAG_application:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name=Data.embedding_model)
        self.persist_directory = Data.persist_directory
        self.db_collection_name = Data.db_collection_name_premier_league
        # Define key phrases that might indicate the start of description or table
        self.description_indicators = [
            "### Description of the Table",
            "### Table Description",
            "### Description of Table",
            "The table presents",
            "This table shows"
        ]
        
        # Table indicators - ways a table section might start
        self.table_indicators = [
            "### Table in Markdown Format",
            "Markdown Table",
            "```markdown",
        ]

    def find_section_boundary(self, content: str, start_idx: int, indicators: List[str]) -> int:
        """
        Find the start of a section by looking for any of the indicator phrases.
        Returns the earliest occurrence after start_idx.
        """
        positions = []
        for indicator in indicators:
            pos = content.find(indicator, start_idx)
            if pos != -1:
                positions.append(pos)
        return min(positions) if positions else -1

    def find_next_section(self, content: str, start_idx: int) -> int:
        """
        Find the start of the next major section (either description or table)
        """
        all_indicators = self.description_indicators + self.table_indicators
        positions = []
        for indicator in all_indicators:
            pos = content.find(indicator, start_idx + 1)  # +1 to avoid finding current section
            if pos != -1:
                positions.append(pos)
        return min(positions) if positions else len(content)

    def split_documents(self, content: str) -> List[Document]:
        """
        Split content into documents, each containing a description and its corresponding table.
        Uses flexible matching to identify sections.
        """
        documents = []
        current_pos = 0
        
        while current_pos < len(content):
            # Find description start
            desc_start = self.find_section_boundary(content, current_pos, self.description_indicators)
            if desc_start == -1:
                break
                
            # Find table start
            table_start = self.find_section_boundary(content, desc_start, self.table_indicators)
            if table_start == -1:
                break
                
            # Find next major section start (for table end)
            # Look for the next "### " after the table
            next_section = content.find("\n### ", table_start)
            if next_section == -1:
                next_section = len(content)
            
            # Extract description and table
            description = content[desc_start:table_start].strip()
            table_content = content[table_start:next_section].strip()
            
            # Ensure we have the complete table content
            if "```markdown" in table_content:
                # If the table content ends with ```, keep it
                if not table_content.rstrip().endswith("```"):
                    # Find the closing ``` after the table content
                    closing_marker = content.find("```", table_start + table_content.find("```markdown") + 10)
                    if closing_marker != -1:
                        table_content = content[table_start:closing_marker + 3].strip()

            # Create document with metadata
            doc = Document(
                page_content=f"{description}\n\n{table_content}",
                metadata={
                    "type": "table_with_description",
                    "has_description": True,
                    "has_table": True,
                }
            )
            documents.append(doc)
            
            current_pos = table_start + len(table_content)
            
        return documents
     
    def create_vector_db(self):
        """
        Create vector store for RAG.
        """
        db = Chroma(
            collection_name=self.db_collection_name,
            embedding_function=self.embedding_model,
            persist_directory=self.persist_directory
        )
    def add_doc_to_vector_db(self, docs: List[Document]):
        """
        Add documents to vector store for RAG.
        """
        try:
            db = Chroma(
                collection_name=self.db_collection_name,
                embedding_function=self.embedding_model,
                persist_directory=self.persist_directory
            )
            db.add_documents(docs)
            db.persist()
        except Exception as e:
            print(f"Error adding documents to vector store: {e}")
        
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