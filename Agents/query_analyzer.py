from .prompts import DetermineUserQuery_template
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from .state import GraphState

class QueryAnalyzer():
    def __init__(self, llm) -> None:        
        UserPrompt = ChatPromptTemplate.from_messages(DetermineUserQuery_template)
        parser = PydanticOutputParser(pydantic_object=GraphState)
        chain = ({"user_query": RunnablePassthrough()}
                 | UserPrompt.partial(format_instructions=parser.get_format_instructions()) 
                 | llm 
                 | parser)
        self.chain = chain
