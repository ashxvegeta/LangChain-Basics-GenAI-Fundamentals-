from secretkey import gemini_api_key
import os
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
# Set environment variable for Gemini
os.environ["GOOGLE_API_KEY"] = gemini_api_key
# Import Gemini LLM from LangChain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

# Define a prompt template with a variable {profession}
prompt = ChatPromptTemplate.from_template("  \"You are a friendly assistant. Give a short career tip (1-2 sentences) for a {profession}.\n\n\"")

final_prompt = prompt.format_messages(profession="Software Engineer")

resopnse = llm.invoke(final_prompt)
print(resopnse.content)