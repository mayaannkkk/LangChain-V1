from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model = "qwen/qwen3.8-27b",
    groq_api_key=os.getenv("GROQ_API_KEY")
)
chat_history = [
    SystemMessage(content= ("You are a helpful assistant"))
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content= user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content= result.content))
    print("AI: ",result.content)

print(chat_history)