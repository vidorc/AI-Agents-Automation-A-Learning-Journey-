from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings =OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents = [
    "Delhi is the capital of india"
    "kolkata is the capital of west bengal"
]

result = embeddings.embed_documents(documents)
print(str(result))