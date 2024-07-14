from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate

# .env 파일 로드
load_dotenv("/home/kevin/projects/llmChatbot/.env")

# LangChain 설정
llm = ChatOpenAI(model_kwargs={"stream": True})
chat_template = ChatPromptTemplate.from_messages(
    [
        # role, message
        ("system", "당신은 친절한 AI 어시스턴트입니다. 당신의 이름은 핑 입니다."),
        ("human", "반가워요!"),
        ("ai", "안녕하세요! 무엇을 도와드릴까요?"),
        ("human", "{user_input}"),
    ]
)
chain = chat_template | llm | StrOutputParser()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

class UserInput(BaseModel):
    user_input: str


@app.post("/stream")
async def stream_response(request: UserInput):
    user_input = request.user_input

    async def response_generator():
        async for token in chain.astream(user_input):
            yield token

    return StreamingResponse(response_generator(), media_type="text/plain")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
