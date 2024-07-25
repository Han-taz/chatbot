from langchain_openai import ChatOpenAI
from app.core.config import current_config

llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=current_config.OPENAI_API_KEY)
