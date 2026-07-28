from langchain_core.messages import HumanMessage

from app.graph.graph_builder import graph

config = {
    "configurable": {
        "thread_id": "customer-1"
    }
}

response = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="What is the status of order 1001?"
            )
        ]
    },
    config=config,
)

response = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="What is its tracking number?"
            )
        ]
    },
    config=config,
)

print("\nSecond Response\n")

for message in response["messages"]:
    print(type(message).__name__)
    print(message)