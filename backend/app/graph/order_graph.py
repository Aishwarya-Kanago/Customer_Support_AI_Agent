from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition

from app.graph.state import AgentState
from app.graph.checkpointer import memory
from app.graph.nodes import agent_node
from app.graph.tool_node import execute_tools

builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.add_node("tools", execute_tools)

builder.add_edge(START, "agent")

builder.add_conditional_edges(
    "agent",
    tools_condition,
)

builder.add_edge("tools", "agent")

order_graph = builder.compile(
    checkpointer=memory
)