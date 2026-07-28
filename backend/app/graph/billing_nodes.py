from app.agents.billing_agent import billing_agent


def billing_node(state):

    response = billing_agent.invoke(state)

    return {
        "messages": [response]
    }