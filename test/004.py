from langchain_google_genai import ChatGoogleGenerativeAI
from IPython.display import display
from IPython.display import Markdown
import textwrap

def to_markdown(text):
    text = text.replace('·', '*')
    return Markdown(textwrap.indent(text, ">", predicate=lambda _: True))

llm = ChatGoogleGenerativeAI(model="gemini-pro")

result = llm.invoke("Que es una silla?")

response = to_markdown(result.content)

print(result.content)
