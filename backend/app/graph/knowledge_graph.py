from langgraph.graph import START, END, StateGraph

from app.graph.state import AgentState
from app.graph.checkpointer import memory
from app.graph.nodes import agent_node

builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)

builder.add_edge(START, "agent")
builder.add_edge("agent", END)

knowledge_graph = builder.compile(
    checkpointer=memory
)