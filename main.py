from secretkey import openapi_key
import os
os.environ["OPENAI_API_KEY"] = openapi_key

# ✅ Use the new import
from langchain_openai import OpenAI  

# Create LLM
llm = OpenAI(temperature=0.9)

# ✅ Instead of calling like a function, use .invoke()
name = llm.invoke("I want to open a restaurant for Indian food. Give me a name for it.")
print(name)
