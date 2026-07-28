from app.graph.order_graph import order_graph
from app.graph.knowledge_graph import knowledge_graph
from app.graph.billing_graph import billing_graph


def order_delegate(state):

    config = {
        "configurable": {
            "thread_id": "order-agent"
        }
    }

    result = order_graph.invoke(
        state,
        config=config,
    )

    return result


def knowledge_delegate(state):

    config = {
        "configurable": {
            "thread_id": "knowledge-agent"
        }
    }

    result = knowledge_graph.invoke(
        state,
        config=config,
    )

    return result


def billing_delegate(state):

    config = {
        "configurable": {
            "thread_id": "billing-agent"
        }
    }

    result = billing_graph.invoke(
        state,
        config=config,
    )

    return result