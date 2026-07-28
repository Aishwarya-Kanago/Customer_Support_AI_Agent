from app.agents.order_agent import order_agent


def order_node(state):

    response = order_agent.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }