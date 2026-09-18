from cryptography.hazmat.primitives.serialization import load_ssh_private_key
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 

load_dotenv()
model = ChatGroq(
    model = "qwen/qwen3.8-27b",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

messages = [
    SystemMessage(content = "You are a helpful assistant"),
    HumanMessage(content = "Tell me about langcahin")
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)