def route_request(state):

    question = state["messages"][-1].content.lower()

    keywords = [

        "refund",
        "return",
        "shipping",
        "delivery",
        "warranty",
        "payment",
        "policy"

    ]

    if any(word in question for word in keywords):
        return "retriever"

    return "agent"


def get_next_graph(route: str):

    if route == "OrderAgent":
        return "order"

    if route == "KnowledgeAgent":
        return "knowledge"

    if route == "BillingAgent":
        return "billing"

    raise ValueError(f"Unknown route: {route}")