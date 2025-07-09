import sys
import asyncio

import aiohttp
from prettytable import PrettyTable
from langchain_core.tools import tool
from .models import Player

from fpl import FPL
from typing import Annotated

async def get_player_by_web_name(player_name: str):
    """
    Fetch a player by their web name from the Fantasy Premier League API.
    The player object contains various attributes such as goals scored, assists, and current cost.
    Args:
        player_name (str): The web name (usually surname) of the player to search for.
    Returns:
        Player object if found, otherwise None.
    """
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()
        for player in players:
            if player.web_name.lower() == player_name.lower():
                returnable_player = Player(**vars(player))
                return returnable_player
    return None

# async def main():
#     player = await get_player_by_web_name("Haaland")
#     #print(player)


# if sys.version_info >= (3, 7):
#     # Python 3.7+
#     asyncio.run(main())
# else:
#     # Python 3.6
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())