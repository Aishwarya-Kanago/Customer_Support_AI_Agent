from langgraph.graph import START, END, StateGraph

from app.graph.state import AgentState
from app.graph.checkpointer import memory

from app.graph.retriever_node import retrieve_documents
from app.graph.knowledge_nodes import knowledge_node

builder = StateGraph(AgentState)

builder.add_node("retriever", retrieve_documents)
builder.add_node("agent", knowledge_node)

builder.add_edge(START, "retriever")
builder.add_edge("retriever", "agent")
builder.add_edge("agent", END)

knowledge_graph = builder.compile(
    checkpointer=memory
)