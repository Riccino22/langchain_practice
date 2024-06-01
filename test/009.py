from langchain_experimental.utilities import PythonREPL
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_groq import ChatGroq

llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

python_repl = PythonREPL()
print(python_repl.run('print([n for n in range(1,100) if n % 13 == 0])'))

agent_executor = create_python_agent(
    llm=llm,
    tool=PythonREPLTool(),
    verbose=True
)

prompt = "Encuentra el promedio de los cubos de los numeros del 1 al 10 y fuerza a que se vean 3 decimales"

respuesta = agent_executor.invoke(prompt)

print("RESPUESTA:")
print(respuesta["output"])