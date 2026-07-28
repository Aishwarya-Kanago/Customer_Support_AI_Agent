from langchain_core.messages import HumanMessage

from app.graph.billing_graph import billing_graph

result = billing_graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="Why did my payment fail?"
            )
        ]
    },
    config={
        "configurable": {
            "thread_id": "customer-1"
        }
    }
)

print(result["messages"][-1].content)