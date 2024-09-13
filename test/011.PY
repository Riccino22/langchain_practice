from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

template = """What is the translation of "{frase}" to english. Your answer must be only:
    (the translation).
 """

llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-pro")

prompt_template = PromptTemplate(input_variables=["frase"], template=template)

print(prompt_template)

chain = LLMChain(llm=llm, prompt=prompt_template)

respuesta = chain.invoke(input={
    "frase": "Tienes mucha razon",
})

print(respuesta)
