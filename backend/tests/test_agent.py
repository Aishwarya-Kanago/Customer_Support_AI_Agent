from app.agents.customer_support_agent import agent

response = agent.invoke(
    "Where is order 1002?"
)

print(response)