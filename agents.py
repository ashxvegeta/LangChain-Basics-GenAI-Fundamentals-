from secretkey import gemini_api_key
import os
os.environ["GOOGLE_API_KEY"] = gemini_api_key

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentType, initialize_agent, load_tools

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
response = agent.invoke("What is the capital of India? Also what is 13*13?")
print(response)