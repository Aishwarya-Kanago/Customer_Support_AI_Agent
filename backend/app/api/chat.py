from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.chain import ask

router = APIRouter(prefix="/api")


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):
    return ask(request.message)