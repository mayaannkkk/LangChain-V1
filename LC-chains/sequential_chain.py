from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

prompt1 = PromptTemplate(
    template="Give me a breif explaination for this {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Give me a 5 important point summary from this {text}",
    input_variables=['text']
)

model = ChatGroq(
    model= "qwen/qwen3.8-27b"
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model |parser

result = chain.invoke({'text' : "Unemployement in india"})

print(result)

chain.get_graph().print_ascii()