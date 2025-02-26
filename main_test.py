from Scrapper.PrimerLeague import PremierLeagueCrawler
from langchain.agents.agent_types import AgentType
from langchain_aws import BedrockLLM
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import boto3

crawler = PremierLeagueCrawler()
#crawler.getTeams()
#crawler.scrap()
df_team = crawler.loadTeamsInfo("Liverpool.csv")

llm = BedrockLLM(model_id="anthropic.claude-v2",
            client=boto3.client(service_name='bedrock-runtime', region_name='us-east-1'),
            model_kwargs={"temperature":0.})

agent = create_pandas_dataframe_agent(
    llm,
    df_team,
    verbose = True,
    agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors = True,
    allow_dangerous_code = True
)

# agent.run("""1. 球隊過去與特定對手交鋒時,分別取得了多少勝,平,負?""")
resp = agent.run("""1. 球隊在主場與客場的對戰表現是否有明顯差異?
             2. 球隊目前總共取得多少勝, 平, 負? 
             """)

print("123")