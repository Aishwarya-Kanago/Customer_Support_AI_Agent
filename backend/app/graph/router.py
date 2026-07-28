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