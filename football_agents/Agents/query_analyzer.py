from ..Prompt.main_prompts import DetermineUserQuery_template
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from ..GraphState.main_state import MainGraphState

class QueryAnalyzer():
    def __init__(self, llm) -> None:        
        UserPrompt = ChatPromptTemplate.from_messages(DetermineUserQuery_template)
        parser = PydanticOutputParser(pydantic_object=MainGraphState)
        chain = ({"user_query": RunnablePassthrough()}
                 | UserPrompt.partial(format_instructions=parser.get_format_instructions()) 
                 | llm 
                 | parser)
        self.chain = chain
