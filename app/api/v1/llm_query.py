from langchain_core.output_parsers import StrOutputParser
from app.core.llm import llm
from app.prompts.llm_qurery_prompt import llm_prompt

chain = llm_prompt|llm|StrOutputParser()

async def get_response(input_text: str):
    async for token in chain.astream({"input": input_text}):
        yield token
