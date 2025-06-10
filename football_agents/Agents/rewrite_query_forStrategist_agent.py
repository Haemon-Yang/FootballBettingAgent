from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from ..GraphState.strategist_state import StrategistState
from ..Prompt import rewrite_query_template

def RewriteQueryForStrategist(llm, state: StrategistState):
    template = ChatPromptTemplate.from_messages(rewrite_query_template)
    parser = StrOutputParser()
    chain = (template | llm | parser)
    result = chain.invoke({"user_query": state.user_query})

    return {
        "rewritten_query": result
    }
