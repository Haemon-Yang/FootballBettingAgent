import json
from langchain_openai import ChatOpenAI
from Scrapper.PrimerLeague import PremierLeagueCrawler
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
import tiktoken
import huggingface_hub
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
import os

load_dotenv()
huggingface_hub.login(token=os.getenv("HUGGINGFACE_API_KEY"))
Chroma_Path = "chroma_db"
Collection_Name = "premier_league_data"

# Prepare the embedding model
## Embedding model - from langchain_huggingface
huggingface_ef = HuggingFaceEmbeddings(
    model_name = "BAAI/bge-small-en-v1.5",
)
def embed_text_langchain_huggingface(text: str):
    return huggingface_ef.embed_query(text)

## Embedding model - directly from huggingface
embedding_model = SentenceTransformer("BAAI/bge-small-en-v1.5")
def embed_text_huggingface(text: str):
    return embedding_model.encode([text], normalize_embeddings=True).tolist()

# Load Data
liverpool_md = PremierLeagueCrawler.load_md_as_str("Teams/liverpool_all_stats.md")
Liverpool_matches = PremierLeagueCrawler.load_md_as_str("Teams/liverpool_matches.md")
Liverpool_standard_stats = PremierLeagueCrawler.load_md_as_str("Teams/liverpool_standard_stats.md")
Liverpool_shooting_stats = PremierLeagueCrawler.load_md_as_str("Teams/liverpool_shooting_stats.md")
# Test the embedding models
embedding_dim_langchain = len(embed_text_langchain_huggingface(liverpool_md))
embedding_dim_huggingface = len(embed_text_huggingface(liverpool_md))
embedding_text_langchain = embed_text_langchain_huggingface(liverpool_md)
embedding_text_huggingface = embed_text_huggingface(liverpool_md)

# Create documents
documents = [
    Document(page_content=Liverpool_standard_stats, metadata={"source": "liverpool_standard_stats_md"}),
    Document(page_content=Liverpool_shooting_stats, metadata={"source": "liverpool_shooting_stats_md"}),
    Document(page_content=Liverpool_matches, metadata={"source": "liverpool_matches_md"}),
]

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

# Create Chroma database with documents
db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name=Collection_Name,
    persist_directory=Chroma_Path
)
db.persist()

# Test query
question = "Who is best shooter in Liverpool FC?"
results = db.similarity_search(
    query=question,
    k=2
)

print(results)
