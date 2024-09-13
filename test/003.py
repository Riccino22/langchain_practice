from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai
import textwrap
import os
load_dotenv()
def to_markdown(text):
    text = text.replace('·', '*')
    return Markdown(textwrap.indent(text, ">", predicate=lambda _: True))

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-pro")

prompt = [
    "What is mixture of experts?",
]

response = model.generate_content(prompt)

print(response.text)