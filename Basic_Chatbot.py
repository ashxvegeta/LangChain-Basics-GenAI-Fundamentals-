from secretkey import gemini_api_key
import os
os.environ["GOOGLE_API_KEY"] = gemini_api_key
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
# Prompt template for Q&A
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("user", "Answer the question below in a concise way:\n\nQuestion: {question}")
])
chain = prompt | llm
while True:
    user_input = input("Ask a question (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    response = chain.invoke({"question": user_input})
    print("AI Answer:", response.content)
