from secretkey import gemini_api_key
import os
os.environ["GOOGLE_API_KEY"] = gemini_api_key

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("user", "Answer the question below in a concise way:\n\nQuestion: {question}")
])

chain = prompt | llm

history = []

while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        break

    full_input = " ".join(history) + "\n" + user_input if history else user_input

    response = chain.invoke({"question": full_input})
    answer = response.content.strip()

    print("AI:", answer)

    history.append(f"User: {user_input}")
    history.append(f"AI: {answer}")
