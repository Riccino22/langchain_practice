from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, AIMessage, HumanMessage
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_react_agent

llm = ChatGroq(model_name="mixtral-8x7b-32768")

search = DuckDuckGoSearchRun()

template = '''
State as precisely as you can, what is the price of the following product:
{q}.
Respond to me with a price for this product, using your criteria to evaluate product prices and information obtained from the Internet.

Respond to me only with the price you assigned to this product. Your response should follow the following structure:

price: (the price you chose) $
'''

for _ in range(2):
    prompt_template = PromptTemplate.from_template(template)

    prompt = hub.pull('hwchase17/react')

    duckduckgo_tool = Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="Useful for searching prices on online sales pages for products accurately and in dollars, usually referencing Amazon, for example."
    )

    tools = [duckduckgo_tool]

    agent = create_react_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=20
    )

    question = 'Office Chair Black'

    output = agent_executor.invoke({
        'input': prompt_template.format(q=question)
    })

    print(output)
