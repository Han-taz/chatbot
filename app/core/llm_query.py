from langchain_core.output_parsers import StrOutputParser
from app.utils.config_openai import llm
from app.template.llm_qurery_prompt import llm_prompt

chain = llm_prompt|llm|StrOutputParser()

def get_response(input_text):
