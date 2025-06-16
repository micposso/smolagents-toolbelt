from fastapi import FastAPI
from pydantic import BaseModel
from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel, ChatMessage
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=Path("../.env"))
api_key = os.getenv("OPENAI_API_KEY")

model = OpenAIServerModel(
    model_id="gpt-3.5-turbo",
    api_key=api_key,
    api_base="https://api.openai.com/v1"
)


# Create agent with system prompt via `task_prompt`
agent = CodeAgent(
    model=model,
    add_base_tools=True,
    tools=[DuckDuckGoSearchTool()],
)

# == FastAPI Setup ==
app = FastAPI()

class Query(BaseModel):
    query: str
    
@app.post("/ask")
def ask_query(query: Query):
    user_input = query.query
    result = agent.run(user_input)
    return {"response": result}
