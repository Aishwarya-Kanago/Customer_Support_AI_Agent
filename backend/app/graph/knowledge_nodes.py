from app.agents.knowledge_agent import knowledge_agent


def knowledge_node(state):

    response = knowledge_agent.invoke(state)

    return {
        "messages": [response]
    }