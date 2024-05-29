from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

API = os.environ.get("API")

print(API)

prompt = PromptTemplate.from_template("Adjetivo {adjetivo}")
print(prompt)

print(prompt.format(adjetivo="fascinante"))