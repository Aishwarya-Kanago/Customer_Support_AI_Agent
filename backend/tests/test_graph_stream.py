from langchain_core.messages import HumanMessage

from app.graph.graph_builder import graph

config = {
    "configurable": {
        "thread_id": "customer-1"
    }
}

for event in graph.stream(
    {
        "messages": [
            HumanMessage(
                content="What is the status of order 1001?"
            )
        ]
    },
    config=config,
    stream_mode="updates",
):
    for node, output in event.items():
        print("=" * 40)
        print(f"Node: {node}")
        print("=" * 40)

        print(output)

        print()