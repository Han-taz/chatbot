from langchain_openai import ChatOpenAI
from app.config import openai_api_key
print("done")

llm = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_api_key)

