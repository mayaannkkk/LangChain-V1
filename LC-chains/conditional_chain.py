from langchain_core.output_parsers import format_instructions
from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGroq(
    model = "qwen/qwen3.8-27b"
)

parser = StrOutputParser()

class feedback(BaseModel):

    sentiment : Literal['positive', 'negative'] = Field(description="It provides the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the feedback into postive or negative \n {feedback} \n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)

classify_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template= "Write a appropriate response of 2 lines to positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template= "Write a appropriate response of 2 lines to negative feedback \n {feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == "positive" , prompt2 | model | parser),
    (lambda x : x.sentiment == "negative" , prompt3 | model | parser),
    RunnableLambda(lambda x:"couldn't find the sentiment")
)

chain = classify_chain | branch_chain

result = chain.invoke({'feedback' : "This phone is terrible"})

print(result)