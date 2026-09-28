from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template="Please give the notes from this {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Please generate a 5 questions quiz from this {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template= "Merge these both {notes} and {quiz} in  a single document",
    input_variables=['notes', 'quiz']
)

model = ChatGroq(
    model= "qwen/qwen3.8-27b"
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes" : prompt1 | model | parser,
    "quiz" : prompt2 | model | parser
}) 

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

text = """
Linear Regression is a machine learning algorithm based on supervised learning. It performs a regression task. Regression models a target prediction value based on independent variables. It is mostly used for finding out the relationship between variables and forecasting. Different regression models differ based on – the kind of relationship between the dependent and independent variables, they are considering and the number of independent variables being used. This article is going to demonstrate how to use the various Python libraries to implement linear regression on a given dataset. We will demonstrate a binary linear model as this will be easier to visualize. In this demonstration, the model will use Gradient Descent to learn."""

result = chain.invoke({'text' : text})

print(result)

chain.get_graph().print_ascii()