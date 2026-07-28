from langgraph.graph import START, END, StateGraph

from app.graph.state import AgentState
from app.graph.billing_nodes import billing_node
from app.graph.checkpointer import memory

builder = StateGraph(AgentState)

builder.add_node("agent", billing_node)

builder.add_edge(START, "agent")
builder.add_edge("agent", END)

billing_graph = builder.compile(
    checkpointer=memory
)