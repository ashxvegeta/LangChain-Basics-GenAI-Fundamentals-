from secretkey import gemini_api_key
import os

# Set environment variable for Gemini
os.environ["GOOGLE_API_KEY"] = gemini_api_key

# Import Gemini LLM from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

# Ask Gemini a question
response = llm.invoke("Give me only ONE short name for an Indian restaurant, nothing else.")



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


name_chain = LLMChain(llm=llm, prompt=PromptTemplate_name)

prompt_template_items = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Give me a list of three {restaurant_name} that are used in Indian cooking. Respond in comma separated format, without any explanation."
)

food_chain = LLMChain(llm=llm, prompt=prompt_template_items)

from langchain.chains import SimpleSequentialChain
sequential_chain = SimpleSequentialChain(chains=[name_chain, food_chain])
response = sequential_chain.run("Indian")
print(response)