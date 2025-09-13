from secretkey import gemini_api_key
import os

# Set environment variable for Gemini
os.environ["GOOGLE_API_KEY"] = gemini_api_key

# Import Gemini LLM from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)

# Ask Gemini a question
response = llm.invoke("Give me only ONE short name for an Indian restaurant, nothing else.")
print(response.content)


from langchain.prompts import PromptTemplate
PromptTemplate_name = PromptTemplate(
    input_variables=["cuisine"],
    template="Give me only ONE short name for a {cuisine} restaurant, nothing else."
)
# prompt = PromptTemplate_name.format(cuisine="Indian")
# print(prompt)
# Fill template
prompt = PromptTemplate_name.format(cuisine="Indian")

# Use template with Gemini
response = llm.invoke(prompt)
print(response.content)