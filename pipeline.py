from typing import Annotated, Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from tools.fpl_loader import get_player_by_web_name, fetch_transfer_trends, fetch_team_fixtures_by_id
from langchain_core.tools import StructuredTool
from typing import Annotated
from tools.team_fixtures import fetch_team_fixtures_using_id, get_head_to_head_results, get_last_results


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

async def main(input_player_name,openai_api_key): 
    llm = ChatOpenAI(
        api_key=openai_api_key,
        model="gpt-4o-mini",
    )

    with open('prompt.md', 'r', encoding='utf-8') as f:
        prompt_from_file = f.read()
    
    prompt_from_file = prompt_from_file.format(Player=input_player_name)

    graph = StateGraph(State)

    get_player_details = StructuredTool.from_function(
        coroutine=get_player_by_web_name,
        name="get_player_by_web_name",
        description="Get player details by web name."
    )
    get_team_fixtures = StructuredTool.from_function(
        coroutine=fetch_team_fixtures_by_id,
        name="fetch_team_fixtures_by_id",
        description="Fetch team fixtures by team ID."
    )

    tools = [get_player_details, 
    fetch_team_fixtures_using_id, 
    get_head_to_head_results,
    get_last_results]
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

    return new_state["messages"][-1].content

if __name__ == "__main__":
    
    import asyncio
    asyncio.run(main())