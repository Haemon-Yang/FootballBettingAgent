from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
# 等等測試bedrock
from langchain_aws import ChatBedrock
import boto3
from graph import Workflow
from colorama import Fore, Style
from pprint import pprint
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
#llm_bedrock = ChatBedrock(model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
#            client=boto3.client(service_name='bedrock-runtime', region_name='us-east-1'),
#            model_kwargs={"temperature":0.})

workflow = Workflow(llm)
state = workflow.get_initial_state()

app = workflow.app

while True:
    user_input = input("Enter a user query: ")
    if user_input == "exit":
        print(Fore.RED + "Exiting..." + Style.RESET_ALL)
        break

    state.update({"user_query": user_input})

    for output in app.stream(state):
        pprint(output)
