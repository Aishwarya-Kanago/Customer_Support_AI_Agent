from langchain_core.messages import SystemMessage

from app.core.model import llm
from app.prompts.supervisor_prompt import SUPERVISOR_PROMPT


class SupervisorAgent:

    def __init__(self):
        self.agent = llm

    def invoke(self, messages):

        messages = [
            SystemMessage(content=SUPERVISOR_PROMPT),
            *messages,
        ]

        return self.agent.invoke(messages)


supervisor_agent = SupervisorAgent()