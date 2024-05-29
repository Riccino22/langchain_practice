##CADENAS CON PROMPT TEMPLATES
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from IPython.display import display
from IPython.display import Markdown
import textwrap
from dotenv import load_dotenv
import os
load_dotenv()

template = "Eres un asistente útil que traduce del {idioma_entrada} al {idioma_salida} el texto {texto}."

prompt_template = PromptTemplate(input_variables=["idioma_entrada", "idioma_salida", "texto"], template=template)

print(prompt_template)

llm_google = ChatGoogleGenerativeAI(model="gemini-pro")
chain = LLMChain(llm=llm_google, prompt=prompt_template)

respuesta = chain.invoke(input={
    "idioma_entrada": "español",
    "idioma_salida": "inglés",
    "texto" : "Me encanta programar"
})

print(respuesta)