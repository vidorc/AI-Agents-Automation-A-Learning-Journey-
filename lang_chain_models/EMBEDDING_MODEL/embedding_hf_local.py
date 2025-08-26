from langchain_huggingface import HuggingFaceEmbeddings
embeddding = HuggingFaceEmbeddings(model_name ='sentence-transformers/all-MiniLM-L6-v2')
text = "Delhi is the capital on India"
