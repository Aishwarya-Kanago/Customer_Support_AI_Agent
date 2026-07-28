from langchain_core.messages import SystemMessage

from app.core.model import llm
from app.tools.tool_registry import tools


class CustomerSupportAgent:

    def __init__(self):
        self.agent = llm.bind_tools(tools)

    def invoke(self, state):

        messages = state["messages"]

        documents = state.get("documents", [])

        if documents:

            context = "\n\n".join(
                doc.page_content
                for doc in documents
            )

            messages = [

                SystemMessage(
                    content=f"""
Use the following context to answer.

Context:

{context}

If the answer isn't in the context,
say you don't know.
"""
                )

            ] + messages

        return self.agent.invoke(messages)


customer_support_agent = CustomerSupportAgent()