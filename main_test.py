from Scrapper.PrimerLeague import PremierLeagueCrawler
from langchain.agents.agent_types import AgentType
from langchain_aws import BedrockLLM
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import boto3

crawler = PremierLeagueCrawler()
#crawler.getTeams()
#crawler.scrap()
Team_Liverpool = crawler.loadTeamsInfo("Liverpool.csv")
Team_Southampton = crawler.loadTeamsInfo("Southampton.csv")

llm = BedrockLLM(model_id="anthropic.claude-v2",
            client=boto3.client(service_name='bedrock-runtime', region_name='us-east-1'),
            model_kwargs={"temperature":0.})

agent = create_pandas_dataframe_agent(
    llm,
    [Team_Liverpool, Team_Southampton],
    verbose = True,
    agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors = True,
    allow_dangerous_code = True,
    response_format = {"type": "json_object"},
    prefix = """
    You are a helpful assistant that can answer questions about the Premier League.
    You are given a list of teams and their information.
    You can answer questions about the teams and their information.
    Answer the question in a scientific way.
    If the data is not enough for you to answer the question, please say "Not enough data to answer the question".
    You must always return valid JSON fenced by a markdown code block. Do not return any additional text.

    Match: Liverpool vs Southampton, First data is Liverpool, Second data is Southampton.
    """,
)

# agent.run("""1. 球隊過去與特定對手交鋒時,分別取得了多少勝,平,負?""")
resp = agent.run("""1. Who will win the match and why?
                 2. How do I win these football games: 1X2, Handicap, Over/Under, Correct Score, Half-Time/Full-Time, Double Chance, and various Goal-Related Bets?
             """)

print(resp)