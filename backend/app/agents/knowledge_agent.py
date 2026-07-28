from app.core.model import llm


class KnowledgeAgent:

    def __init__(self):
        self.agent = llm

    def invoke(self, messages):
        return self.agent.invoke(messages)


knowledge_agent = KnowledgeAgent()