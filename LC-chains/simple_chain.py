from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

prompt = PromptTemplate(
    template="Please give 5 lines poem about {topic}",
    input_variables=['topic']
)

model = ChatGroq(
    model= "qwen/qwen3.8-27b"
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic' : "cricket"})

print(result)

chain.get_graph().print_ascii()