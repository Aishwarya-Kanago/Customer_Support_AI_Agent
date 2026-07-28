from fastapi import FastAPI

from app.api.chat import router as chat_router

app = FastAPI(title="Customer Support AI")

app.include_router(chat_router)