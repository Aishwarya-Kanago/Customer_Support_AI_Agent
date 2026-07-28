from app.core.model import llm


class BillingAgent:

    def __init__(self):
        self.agent = llm

    def invoke(self, messages):
        return self.agent.invoke(messages)


billing_agent = BillingAgent()