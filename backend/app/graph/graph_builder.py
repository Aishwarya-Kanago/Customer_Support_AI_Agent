from langgraph.graph import START, END, StateGraph

from app.graph.state import AgentState
from app.graph.nodes import agent_node
from app.graph.tool_node import execute_tools
from app.graph.retriever_node import retrieve_documents
from app.graph.router import route_request
from app.graph.checkpointer import memory

builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.add_node("tools", execute_tools)
builder.add_node("retriever", retrieve_documents)

builder.add_conditional_edges(
    START,
    route_request,
)

builder.add_edge("retriever", "agent")

builder.add_conditional_edges(
    "agent",
    lambda state: "tools" if state["messages"][-1].tool_calls else END,
)

builder.add_edge("tools", "agent")

graph = builder.compile(
    checkpointer=memory
)