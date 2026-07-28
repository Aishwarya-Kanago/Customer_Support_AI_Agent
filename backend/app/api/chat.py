from fastapi import APIRouter
from langchain_core.messages import HumanMessage

from app.schemas.chat_request import ChatRequest
from app.schemas.chat_response import ChatResponse
from app.graph.supervisor_graph import supervisor_graph
from app.utils.message_utils import extract_text

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    config = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    result = supervisor_graph.invoke(
        {
            "messages": [
                HumanMessage(content=request.message)
            ]
        },
        config=config,
    )

    last_message = result["messages"][-1]
    response = extract_text(last_message)

    return ChatResponse(response=response)