from langchain_core.messages import ToolMessage

from app.tools.tool_registry import TOOLS

import json


def execute_tools(ai_message):
    """
    Execute all requested tool calls and return ToolMessage objects.
    """

    tool_messages = []

    for tool_call in ai_message.tool_calls:

        tool_name = tool_call["name"]

        tool_args = tool_call["args"]

        tool = TOOLS[tool_name]

        result = tool.invoke(tool_args)

        tool_messages.append(
            ToolMessage(
                content=json.dumps(result),
                tool_call_id=tool_call["id"],
            )
        )

    return tool_messages