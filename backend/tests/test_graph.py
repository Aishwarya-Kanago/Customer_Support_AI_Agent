from langchain_core.messages import HumanMessage

from app.graph.graph_builder import graph

config = {
    "configurable": {
        "thread_id": "customer-1"
    }
}

result = graph.invoke(
    {
        "messages": [
            HumanMessage(content="What is your refund policy?")
        ]
    },
    config=config,
)

for message in result["messages"]:
    print(type(message).__name__)
    if isinstance(message.content, list):
        for part in message.content:
            if part.get("type") == "text":
                print(part["text"])
    else:
        print(message.content)