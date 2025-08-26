from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4",
    temperature=1.5,
    max_completion_tokens=10
)

result = model.invoke("Write 5 lines on cricket")

print(result.content)
