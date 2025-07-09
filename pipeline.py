from typing import Annotated, Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from tools.fpl_loader import get_player_by_web_name
from langchain_core.tools import StructuredTool
from typing import Annotated
import os
from dotenv import load_dotenv

class State(TypedDict):
    messages: Annotated[list, add_messages]
    
def prompt_node(state: State) -> State:
    new_message = llm_with_tools.invoke(state["messages"])
    return {"messages": [new_message]}

def conditional_edge(state: State) -> Literal['tool_node', '__end__']:
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tool_node"
    else:
        return "__end__"

async def main(): 
    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model=os.environ.get("MODEL"),
    )

    with open('prompt.md', 'r', encoding='utf-8') as f:
        prompt_from_file = f.read()

    graph = StateGraph(State)

    get_player_details = StructuredTool.from_function(
        coroutine=get_player_by_web_name,
        name="get_player_by_web_name",
        description="Get player details by web name."
    )

    tools = [get_player_details]
    llm_with_tools = llm.bind_tools(tools)

    def prompt_node(state: State) -> State:
        new_message = llm_with_tools.invoke(state["messages"])
        return {"messages": [new_message]}

    tool_node = ToolNode(tools)

    graph.add_node("tool_node", tool_node)
    graph.add_node("prompt_node", prompt_node)
    graph.add_conditional_edges('prompt_node', conditional_edge)
    graph.add_edge("tool_node", "prompt_node")
    graph.set_entry_point("prompt_node")

    APP = graph.compile()

    new_state = await APP.ainvoke({"messages": [prompt_from_file]})

    print(new_state["messages"][-1].content)

if __name__ == "__main__":
    load_dotenv()
    import asyncio
    asyncio.run(main())