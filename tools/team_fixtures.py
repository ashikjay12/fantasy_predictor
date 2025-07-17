from football import Football
from tools.models import Teams
#from models import Teams
from enum import IntEnum
import requests
from dateutil import parser
from langchain_core.tools import tool

API_KEY = ""
HEADERS = {"X-Auth-Token": API_KEY}
BASE_URL = 'https://api.football-data.org/v4'

def fetch_team_fixtures_using_id(input_team_id):

    """ Fetch upcoming fixtures for a team by its ID.
    Args:   
        input_team_id (int): The ID of the team to fetch fixtures for.
    Returns:
        list: A list of upcoming fixtures for the team.
    """

    API_KEY = ""
    HEADERS = {"X-Auth-Token": API_KEY}
    BASE_URL = 'https://api.football-data.org/v4'

    TEAM_NAME_TO_ID = {
    'Arsenal FC': 57,
    'Chelsea FC': 61,
    'Liverpool FC': 64,
    'Manchester United FC': 66,
    'Manchester City FC': 65,
    'Tottenham Hotspur FC': 73,
    # Add others as needed
}
    #selected_team = get_team_name(input_team_id)
    team_name = Teams(input_team_id).name.replace('_', ' ')
    #print(f"Fetching fixtures for team: {team_name}")
    
    # Try to find the actual API team ID from name
    team_api_id = None
    for name, tid in TEAM_NAME_TO_ID.items():
        if team_name.lower() in name.lower():
            team_api_id = tid
            break

    if not team_api_id:
        raise ValueError(f"Team '{team_name}' not found in API ID map.")

    # Request upcoming matches
    url = f"{BASE_URL}/teams/{team_api_id}/matches?status=SCHEDULED&limit=5"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    #print(f"Response data: {data}")
    print(f"Next fixtures for {team_name.replace('_', ' ')}:")
    matches = []
    match_dict = {}
    for match in data.get('matches', []):
        match_dict["date"] = f"{parser.parse(match['utcDate'])}"
        match_dict["home"] = match['homeTeam']['name']
        match_dict["away"] = match['awayTeam']['name']
        matches.append(match_dict.copy())
        print("fetched")
    #print(matches)
    return matches

TEAM_NAME_TO_ID = {
    'Arsenal': 57,
    'Aston Villa FC': 58,
    'Brentford FC': 402,
    'Brighton': 397,
    'Burnley FC': 328,
    'Chelsea': 61,
    'Crystal Palace FC': 354,
    'Everton FC': 62,
    'Leicester FC': 338,
    'Leeds FC': 341,
    'Liverpool': 64,
    'Manchester City FC': 65,
    'Manchester United': 66,
    'Newcastle United FC': 67,
    'Norwich City FC': 68,
    'Southampton FC': 340,
    'Tottenham': 73,
    'Watford FC': 346,
    'West Ham FC': 563,
    'Wolverhampton Wanderers': 76
}

def get_head_to_head_results(team1_name: str, team2_name: str, limit: int = 5):
    """
    Return a list of past match results between two teams.
    Args:
        team1_name (str): Name of the first team.
        team2_name (str): Name of the second team.
        limit (int): Number of past matches to return.
    Returns:
        list: A list of dictionaries containing match date, home team, away team, and scores.
    """
    print("Fetching head-to-head results between", team1_name, "and", team2_name)
    id1 = TEAM_NAME_TO_ID.get(team1_name)
    id2 = TEAM_NAME_TO_ID.get(team2_name)
    #print(f"Team IDs: {id1}, {id2}")
    if not id1 or not id2:
        print(f"Error: One or both teams not found in TEAM_NAME_TO_ID: '{team1_name}', '{team2_name}'")
        raise ValueError(f"One or both teams not found in TEAM_NAME_TO_ID: '{team1_name}', '{team2_name}'")

    url = f"{BASE_URL}/teams/{id1}/matches?opponents={id2}&limit={limit}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    #print(f"Response data: {data}")

    matches = data.get('matches', [])
    results = []

    for match in matches:
        results.append({
            "date": parser.parse(match['utcDate']).strftime("%Y-%m-%d"),
            "home_team": match['homeTeam']['name'],
            "away_team": match['awayTeam']['name'],
            "home_score": match['score']['fullTime']['home'],
            "away_score": match['score']['fullTime']['away'],
        })
    print(f"Found {len(results)} matches")
    return results

def get_last_results(team_name: str, limit: int = 5):
    """Return the last 'limit' match results for the given team.
    Args:
        team_name (str): Name of the team.
        limit (int): Number of past matches to return.
    Returns:
        list: A list of dictionaries containing match date, home team, away team, and scores.
    """
    print(f"Fetching last {limit} results for team: {team_name}")
    team_id = TEAM_NAME_TO_ID.get(team_name)
    if not team_id:
        raise ValueError(f"Team '{team_name}' not found in TEAM_NAME_TO_ID")

    url = f"{BASE_URL}/teams/{team_id}/matches?limit={limit}&season=2024"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    matches = data.get('matches', [])
    results = []

    for match in matches:
        results.append({
            "date": parser.parse(match['utcDate']).strftime("%Y-%m-%d"),
            "home_team": match['homeTeam']['name'],
            "away_team": match['awayTeam']['name'],
            "home_score": match['score']['fullTime']['home'],
            "away_score": match['score']['fullTime']['away'],
        })

    print(f"Found {len(results)} matches for {team_name}")

    return results

# def fetch_team_fixtures_using_id(input_team_id: int):
#     """ Fetch upcoming fixtures for a team by its ID.
#     Args:
#         input_team_id (int): The ID of the team to fetch fixtures for.
#     Returns:
#         list: A list of upcoming fixtures for the team.
#     """

#     selected_team = get_team_name(input_team_id)

#     # Initialize with your API key
#     api = Football(api_token=FOOTBALL_TOKEN)

#     # Get info about Premier League teams
#     teams = api.teams(competition_id=2021)['teams']

#     # Pick a team, e.g., Arsenal
#     selected_team = next(team for team in teams if team['name'] == selected_team)
#     team_id = selected_team['id']

#     # Get upcoming fixtures for Arsenal
#     matches = api.team_matches(team_id=team_id, status='SCHEDULED')

#     # Print next 5 fixtures
#     for match in matches['matches'][:5]:
#         home = match['homeTeam']['name']
#         away = match['awayTeam']['name']
#         date = match['utcDate']
#         print(f"{date} - {home} vs {away}")
#     return matches['matches'][:5]


def get_team_name(team_id: int) -> str:
    """
    Get the name of the team by its ID.
    Args:
        team_id (int): The ID of the team.
    Returns:
        str: The name of the team.
    """
    return Teams(team_id)

# if __name__ == "__main__":
#     # Example usage
#     get_last_results("Arsenal", limit=5)
#     # for fixture in fixtures:
#     #     print(fixture)