from secretkey import gemini_api_key
import os
os.environ["GOOGLE_API_KEY"] = gemini_api_key
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import json

class Analysis(BaseModel):
    summary: str = Field(description="One-sentence summary of the text")
    keywords: list[str] = Field(description="Important keywords from the text")
    sentiment: str = Field(description="Sentiment of the text: positive, negative, or neutral")
    category: str = Field(description="General category of the text, e.g. programming, finance, sports, etc.")


parser = PydanticOutputParser(pydantic_object=Analysis)

# Step 2: LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0)


# Step 3: Prompt

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that analyzes text."),
    ("user", "Analyze the following text:\n\n{text}\n\n{format_instructions}")
])


chain = prompt | llm | parser


# Step 4: Run with sample text
text = "Python, pandas, and LangChain are valuable tools for data analysis and connecting LLMs to data."
response = chain.invoke({"text": text, "format_instructions": parser.get_format_instructions()})


# Step 5: Print results
print("Parsed Output:\n", response.dict())

