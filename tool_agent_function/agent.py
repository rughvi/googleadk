from google.adk.agents import Agent
import requests
url = "https://bored-api.appbrewery.com/random"

def get_bored_ideas() -> dict :
    response = requests.get(url)
    return response.json()

root_agent = Agent(
    name="tool_agent_googlesearch",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_bored_ideas
    """,
    tools=[get_bored_ideas],
)