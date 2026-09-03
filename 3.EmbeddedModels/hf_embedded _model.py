from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "My name is Ned Stark and I am the Lord of Winterfell."

vector = embedding.embed_query(text)

print(str(vector))