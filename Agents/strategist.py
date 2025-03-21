from .state import GraphState
from .prompts import strategist_template
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

class Strategist():
    def __init__(self, llm):
        UserPrompt = ChatPromptTemplate.from_messages(strategist_template)
        parser = StrOutputParser()
        chain = (UserPrompt
            | llm
            | parser
        )
        self.chain = chain