from langgraph.graph import START, END, StateGraph

from app.graph.state import AgentState
from app.graph.checkpointer import memory

builder = StateGraph(AgentState)

builder.add_edge(START, END)

supervisor_graph = builder.compile(
    checkpointer=memory
)