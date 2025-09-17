from secretkey import gemini_api_key
import os
os.environ["GOOGLE_API_KEY"] = gemini_api_key

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentType, initialize_agent, load_tools

# 1. Load Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

# 2. Load extra tools (Wikipedia + math)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# 3. Initialize an agent that can combine reasoning + tool use
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# 4. Run a query (the agent decides what tools to use)
response = agent.run("What is the capital of India? Also what is 13*13?")

print(response)
