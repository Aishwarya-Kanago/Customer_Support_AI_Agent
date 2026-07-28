from app.agents.customer_support_agent import customer_support_agent


def agent_node(state):

    response = customer_support_agent.invoke(state)

    return {
        "messages": [response]
    }