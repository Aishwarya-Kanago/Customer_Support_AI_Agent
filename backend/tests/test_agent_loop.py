from app.api.chat import ChatRequest, chat
        
response = chat(
    ChatRequest(message="Where is my order?")
)

print(response)