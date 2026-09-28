from regex import template
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

parser = StrOutputParser()
model = ChatGroq(
    model= 'qwen/qwen3.8-27b'
)

prompt1 = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)

promt2 = PromptTemplate(
    template="could you please explain the following joke - {text}",
    input_variables=['text']
)

chain = RunnableSequence(prompt1, model, parser,promt2, model, parser)

result = chain.invoke({'topic' : 'AI'})

print(result)