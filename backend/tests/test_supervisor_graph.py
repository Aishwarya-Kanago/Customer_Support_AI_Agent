from langchain_core.messages import HumanMessage

from app.graph.supervisor_graph import supervisor_graph

config = {
    "configurable": {
        "thread_id": "customer-1"
    }
}

result = supervisor_graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="Where is order 1001?"
            )
        ]
    },
    config=config,
)

for message in result["messages"]:
    print(type(message).__name__)

    if hasattr(message, "text"):
        print(message.text)

    else:
        print(message.content)

    print("-" * 40)