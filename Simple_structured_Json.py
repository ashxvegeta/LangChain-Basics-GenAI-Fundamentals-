from secretkey import gemini_api_key
import os
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import json

# Set environment variable for Gemini
os.environ["GOOGLE_API_KEY"] = gemini_api_key
# set llm
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

# Define a prompt
prompt ="""
You are a JSON-only responder. Given the input text, return a JSON object with keys:
- "summary" (string, 1 sentence)
- "keywords" (array of 3 short strings)

Input: "Python and pandas are great for data analysis, and LangChain helps connect LLMs to data."
"""

response = llm.invoke(prompt)
#  removes whitespace at the start/end so parsing or comparisons are cleaner.
text = response.content.strip()
# print("RAW:\n", text)

# RAW:
#  ```json
# {
#   "summary": "Python, pandas, and LangChain are valuable tools for data analysis and connecting LLMs to data.",
#   "keywords": ["Python", "pandas", "LangChain"]
# }
# ```

# What happened:

# Gemini returned valid JSON but wrapped it in a json ... code block.

# json.loads() can’t handle the extra backticks and json language hint.

# We just need to strip those markers before parsing.

# Replace the parsing block with this:

if text.startswith("```"):
       # Remove ```json ... ``` wrappers
       text = text.strip("`")
       if text.lower().startswith("json"):
           text = text[4:].strip()
print("CLEANED:\n", text)

try:
    parsed = json.loads(text)
    print("\nParsed JSON:")
    print(parsed)
except json.JSONDecodeError as e:
    print("\nStill not valid JSON. Error:", e)
    print("Raw text was:\n", text)