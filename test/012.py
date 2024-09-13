from langchain_groq import ChatGroq

llm = ChatGroq()

output = llm.invoke("dime que es un perro", temperature=0.1)

print(output)