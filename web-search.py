from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

model = OpenAIServerModel(
    model_id="gpt-3.5-turbo",
    api_key=api_key,
    api_base="https://api.openai.com/v1"
)

agent = CodeAgent(
    model=model,
    add_base_tools=True,
    tools=[DuckDuckGoSearchTool()]
)

response = agent.run("Search for a Python library to process CSV files and show me how to use it.")
print(response)
