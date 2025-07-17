import sys
import asyncio

import aiohttp
from prettytable import PrettyTable
from langchain_core.tools import tool
from tools.models import Player

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

async def fetch_team_fixtures_by_id(team_id: int):
    """
    Fetch a team by its ID from the Fantasy Premier League API.
    Args:
        team_id (int): The ID of the team to fetch.
    Returns:
        Team object if found, otherwise None.
    """
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        team = await fpl.get_team(team_id)
        fixtures = await team.get_fixtures()
        print(f"Fixtures for team ID {team_id}:")
        print(fixtures)
        return fixtures

def fetch_transfer_trends(player):
    """ Fetch transfer trends for a player.
    Args:
        player (Player): The player object to fetch trends for.
    Returns:
        dict: A dictionary containing transfers in and out for the current gameweek.
    """

    return {
        "transfers_in": player.transfers_in_event,
        "transfers_out": player.transfers_out_event,
        "selected_by_percent": player.selected_by_percent,
    }

async def main():
     player = await get_player_by_web_name("Haaland")
     print(fetch_transfer_trends(player))
#     #print(player)


if sys.version_info >= (3, 7):
    # Python 3.7+
    asyncio.run(main())
# else:
#     # Python 3.6
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())