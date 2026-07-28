from langgraph.graph import START, END, StateGraph

from app.graph.state import AgentState
from app.graph.checkpointer import memory

from app.graph.supervisor_nodes import supervisor_node
from app.graph.delegate_nodes import billing_delegate, knowledge_delegate, order_delegate

builder = StateGraph(AgentState)

builder.add_node("supervisor", supervisor_node)
builder.add_node(
    "order",
    order_delegate,
)
builder.add_node(
    "knowledge",
    knowledge_delegate,
)
builder.add_node(
    "billing",
    billing_delegate,
)

builder.add_edge(START, "supervisor")

builder.add_edge("order", END)
builder.add_edge("knowledge", END)
builder.add_edge("billing", END)

supervisor_graph = builder.compile(
    checkpointer=memory
)