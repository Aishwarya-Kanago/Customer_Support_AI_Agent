from langgraph.types import Command

from app.agents.supervisor_agent import supervisor_agent


def supervisor_node(state):

    response = supervisor_agent.invoke(
        state["messages"]
    )

    decision = response.text.strip()

    if decision == "OrderAgent":
        return Command(goto="order")

    if decision == "KnowledgeAgent":
        return Command(goto="knowledge")

    if decision == "BillingAgent":
        return Command(goto="billing")

    raise ValueError(f"Unknown agent: {decision}")