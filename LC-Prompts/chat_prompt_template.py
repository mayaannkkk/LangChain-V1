from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ( 'system', "You are a {domain} assistant"),
    ('human', "What the averae area of {topic} ground")
])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'test'})

print(prompt)