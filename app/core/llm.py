from langchain_openai import ChatOpenAI
from app.core.config import current_config
print(f"OpenAI API Key: {current_config.OPENAI_API_KEY}")  # 추가된 출력문
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=current_config.OPENAI_API_KEY)
