from app.core.model import llm
from app.tools.tool_registry import tools


class OrderAgent:

    def __init__(self):
        self.agent = llm.bind_tools(tools)

    def invoke(self, messages):
        return self.agent.invoke(messages)


order_agent = OrderAgent()