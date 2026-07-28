from langchain_core.messages import SystemMessage

from app.core.model import llm


class KnowledgeAgent:

    def __init__(self):
        self.agent = llm

    def invoke(self, state):
        documents = state.get("documents", [])

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        messages = [
            SystemMessage(
                content=f"""
Use the following context to answer the user's question.

Context:
{context}

If the answer is not present in the context, say you don't know.
"""
            ),
            *state["messages"],
        ]

        return self.agent.invoke(messages)


knowledge_agent = KnowledgeAgent()