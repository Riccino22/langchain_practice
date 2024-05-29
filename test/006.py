##CADENAS CON PROMPT TEMPLATES
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from IPython.display import display
from IPython.display import Markdown
import textwrap
from bs4 import BeautifulSoup
import requests

def to_markdown(text):
    text = text.replace('·', '*')
    return Markdown(textwrap.indent(text, ">", predicate=lambda _: True))

template = """Te voy a mandar una palabra en ingles, y seguidamente me mandaras la traduccion al español, el concepto en ingles, y 3 ejemplos de oraciones que usen esa palabra en ingles y al lado entre parentesis su traduccion es español. La respuesta debe seguir la siguiente estructura:
Concept: (colocar en ingles la definicion de la palabra)
Translation: (Aqui va la traduccion al español)
Examples:
1. Aqui va la primera oracion en ingles (Aqui la traduccion de la oracion al español)
2. Aqui va la segunda oracion en ingles (Aqui la traduccion de la oracion al español)
3. Aqui va la tercera oracion en ingles (Aqui la traduccion de la oracion al español)

Esa es la estructura a seguir. La palabra es: {respuesta}
"""

prompt_template = PromptTemplate(input_variables=["respuesta"], template=template)

llm_google = ChatGoogleGenerativeAI(model="gemini-pro")
chain = LLMChain(llm=llm_google, prompt=prompt_template)

word = input("Search a word: ")
respuesta = chain.invoke(input={
    "respuesta": word
})

print(respuesta["text"].replace("*",""))