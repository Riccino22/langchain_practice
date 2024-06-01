from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.sequential import SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

llm_google1 = ChatGoogleGenerativeAI(model="gemini-pro")

prompt_template1 = PromptTemplate.from_template(
    template="""Dame el nombre de 4 personajes famosos de la siguiente epoca y area:
        Epoca: {epoca}
        Area: Ciencias
    """
)

chain1 = LLMChain(
    llm=llm_google1,
    prompt=prompt_template1,
)
llm_google2 = ChatGoogleGenerativeAI(model="gemini-pro")
prompt_template2 = PromptTemplate.from_template(
    template="""Describe la historia e importancia de cada uno de estos personajes en forma de poema:
    {personajes}
    """
)

chain2 = LLMChain(
    llm=llm_google2,
    prompt=prompt_template2,
)

overall_chain = SimpleSequentialChain(chains=[chain1, chain2], verbose=True)

output = overall_chain.invoke("Antigua Grecia")

