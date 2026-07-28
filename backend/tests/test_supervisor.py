from langchain_core.messages import HumanMessage

from app.agents.supervisor_agent import supervisor_agent

response = supervisor_agent.invoke(
    [
        HumanMessage(
            content="Where is order 1001?"
        )
    ]
)

print(response.content)