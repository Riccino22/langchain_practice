from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import llm

llm_google = ChatGoogleGenerativeAI(model="gemini-pro")

template = """Vas a decirme un personaje famoso de la epoca de {epoca} en el area de {area}"""

prompt_template = PromptTemplate.from_template(template=template)

chain = llm.LLMChain(
    llm=llm_google,
    prompt=prompt_template,
    verbose=True
)

output = chain.invoke({
    'epoca': 'Renacimiento',
    'area':'Ciencia'
})

print(output)