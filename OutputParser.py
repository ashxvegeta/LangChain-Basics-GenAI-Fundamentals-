from secretkey import gemini_api_key
import os
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# 1. Define the schema
schema = [
    ResponseSchema(name="summary", description="Short summary of the input text"),
    ResponseSchema(name="keywords", description="List of important keywords")
]   

# 2. Create parser
parser = StructuredOutputParser.from_response_schemas(schema)
format_instructions = parser.get_format_instructions()

# Set environment variable for Gemini
os.environ["GOOGLE_API_KEY"] = gemini_api_key
# set llm
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

# Define a prompt
prompt = PromptTemplate(
    template="Summarize this text and extract keywords:\n{text}\n{format_instructions}",
    input_variables=["text"],
    partial_variables={"format_instructions": format_instructions}
)

# 5. Run chain (Prompt → Gemini → Parser)
chain = prompt | llm | parser

response = chain.invoke({
    "text": "Python, pandas, and LangChain are valuable tools for data analysis and connecting LLMs to data."
})

print("Parsed Output:\n", response)