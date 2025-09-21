from secretkey import gemini_api_key
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set environment variable for Gemini
os.environ["GOOGLE_API_KEY"] = gemini_api_key

# Import Gemini LLM from LangChain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

response = llm.invoke("Explain AI to me like I’m 12 years old.")
print(response.content)