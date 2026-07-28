from app.core.model import llm


class SupervisorAgent:

    def __init__(self):
        self.agent = llm

    def invoke(self, messages):
        return self.agent.invoke(messages)


supervisor_agent = SupervisorAgent()