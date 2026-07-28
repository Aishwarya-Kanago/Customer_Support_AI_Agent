from langchain_core.messages import SystemMessage

from app.core.model import llm
from app.prompts.billing_prompt import BILLING_PROMPT


class BillingAgent:

    def __init__(self):
        self.agent = llm

    def invoke(self, state):
        messages = [
            SystemMessage(content=BILLING_PROMPT),
            *state["messages"],
        ]

        return self.agent.invoke(messages)


billing_agent = BillingAgent()