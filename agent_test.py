from secretkey import gemini_api_key, serpapi_api_key
import os

# Set environment variables
os.environ["GOOGLE_API_KEY"] = gemini_api_key     # For Gemini
os.environ["SERPAPI_API_KEY"] = serpapi_api_key   # For SerpAPI

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentType, initialize_agent
from langchain_community.tools import load_tools  # ✅ Correct import

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

# Load tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Create agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# Run query
response = agent.invoke("What is the capital of India? Also what is 13*13?")
print(response["output"])