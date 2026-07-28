from langchain_core.messages import ToolMessage

from app.tools.tool_registry import tools

import json

tool_map = {
    tool.name: tool
    for tool in tools
}


def execute_tools(state):
    messages = state["messages"]

    last_message = messages[-1]

    tool_messages = []

    for tool_call in last_message.tool_calls:

        tool = tool_map[tool_call["name"]]

        result = tool.invoke(tool_call["args"])

        tool_messages.append(
            ToolMessage(
                content=json.dumps(result),
                tool_call_id=tool_call["id"],
            )
        )

    return {
        "messages": tool_messages
    }