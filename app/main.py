from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api.v1.llm_query import get_response
import uvicorn

# .env 파일 로드
load_dotenv("/mnt/d/dev_sh/Gitlab_sh/chatbot/.env")

# FastAPI 애플리케이션 초기화
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

# llm_query 모듈에서 get_response 함수 임포트


@app.post("/stream")
async def stream_response(request: UserInput):
    user_input = request.user_input

    async def response_generator():
        async for token in get_response(user_input):
            yield token

    return StreamingResponse(response_generator(), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
