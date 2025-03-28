from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from RAG import Data as RAG_data
import pprint

def test_chroma_retrieval():
    # Initialize the embedding model
    embedding_function = HuggingFaceEmbeddings(model_name=RAG_data.embedding_model)
    
    # Connect to your Chroma DB
    vector_store = Chroma(
        persist_directory=RAG_data.persist_directory,
        embedding_function=embedding_function,
        collection_name="premier_league_data"  # Make sure this matches your collection name
    )
    
    # Test queries
    queries = [
        "Brighton vs Fulham match on December 5 2024",
        "match between Brighton and Fulham",
        "Fulham Brighton 2024",
        "December 5 football match"
    ]
    
    for query in queries:
        print(f"\n{'='*80}\nQUERY: {query}\n{'='*80}")
        docs = vector_store.similarity_search(query, k=5)  # Get top 5 results
        
        if not docs:
            print("No documents retrieved!")
        
        for i, doc in enumerate(docs):
            print(f"\nDocument {i+1}:")
            print(f"Content: {doc.page_content}")
            print(f"Metadata: {doc.metadata}")
            print(f"Similarity score: {doc.metadata.get('score', 'N/A')}")
            print("-" * 50)
    
    # Optional: List all documents containing "Brighton" and "Fulham"
    print("\n\nListing ALL documents containing Brighton and Fulham:")
    all_brighton = vector_store.similarity_search("Brighton", k=100)
    all_fulham = vector_store.similarity_search("Fulham", k=100)
    
    print(f"Total Brighton documents: {len(all_brighton)}")
    print(f"Total Fulham documents: {len(all_fulham)}")
    
    # Check for documents containing both teams
    brighton_content = [doc.page_content.lower() for doc in all_brighton]
    fulham_content = [doc.page_content.lower() for doc in all_fulham]
    
    brighton_fulham_docs = [doc for doc in all_brighton if "fulham" in doc.page_content.lower()]
    
    print(f"\nDocuments mentioning both Brighton and Fulham: {len(brighton_fulham_docs)}")
    for doc in brighton_fulham_docs:
        print("-" * 80)
        print(doc.page_content)

if __name__ == "__main__":
    test_chroma_retrieval()