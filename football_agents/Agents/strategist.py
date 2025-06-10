from ..GraphState.main_state import MainGraphState
from ..Prompt import strategist_template, interpret_query_prompt
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_community.vectorstores import Chroma
from ..RAG.Data import db_collection_name_premier_league
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI

class Strategist():
    def __init__(self, llm):
        prompt = ChatPromptTemplate.from_messages(strategist_template)
        parser = StrOutputParser()
        chain = (
            {"teams_data": RunnablePassthrough(), "user_query": RunnablePassthrough()}
            #| RunnableLambda(debug_retrieval)
            | prompt
            | llm
            | parser
        )
        self.chain = chain

def debug_retrieval(inputs):
    docs = inputs["teams_data"]
    print(f"Retrieved {len(docs)} documents:")
    for i, doc in enumerate(docs):
        print(f"Document {i+1}:")
        print(f"Content: {doc.page_content}...")  # Print first 100 chars
        print(f"Metadata: {doc.metadata}")
        print("-" * 50)
    return inputs