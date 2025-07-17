from pydantic import BaseModel, Field
from enum import Enum, IntEnum
from typing import Optional


# class Player(BaseModel):
#     id: int = Field(..., description="Unique identifier for the player")
#     name: str = Field(..., description="Name of the player")
#     position: str = Field(..., description="Position of the player")
#     team: str = Field(..., description="Team of the player")
#     points: float = Field(..., description="Fantasy points scored by the player")
#     status: str = Field(..., description="Current status of the player (e.g., active, injured)")

class Player(BaseModel):
    chance_of_playing_next_round: Optional[int] = Field(
        default=None, description="Chance of playing next round (percent, or None if unknown)"
    )
    chance_of_playing_this_round: Optional[int] = Field(
        default=None, description="Chance of playing this round (percent, or None if unknown)"
    )
    code: Optional[int] = Field(
        default=None, description="Unique FPL code for the player"
    )
    cost_change_event: Optional[int] = Field(
        default=None, description="Cost change in the current event (in tenths of a million)"
    )
    cost_change_event_fall: Optional[int] = Field(
        default=None, description="Cost decrease in the current event (in tenths of a million)"
    )
    cost_change_start: Optional[int] = Field(
        default=None, description="Total cost change since season start (in tenths of a million)"
    )
    cost_change_start_fall: Optional[int] = Field(
        default=None, description="Total cost decrease since season start (in tenths of a million)"
    )
    dreamteam_count: Optional[int] = Field(
        default=None, description="Number of times selected in the Dream Team"
    )
    element_type: Optional[int] = Field(
        default=None, description="Player's position type (1=GK, 2=DEF, 3=MID, 4=FWD)"
    )
    ep_next: Optional[str] = Field(
        default=None, description="Expected points next round"
    )
    ep_this: Optional[str] = Field(
        default=None, description="Expected points this round"
    )
    event_points: Optional[int] = Field(
        default=None, description="Points scored in the current event/gameweek"
    )
    first_name: Optional[str] = Field(
        default=None, description="Player's first name"
    )
    form: Optional[str] = Field(
        default=None, description="Player's current form (recent points per match)"
    )
    id: Optional[int] = Field(
        default=None, description="Unique player ID"
    )
    in_dreamteam: Optional[bool] = Field(
        default=None, description="Is the player in the current Dream Team?"
    )
    news: Optional[str] = Field(
        default=None, description="Latest news about the player (injury, etc.)"
    )
    news_added: Optional[str] = Field(
        default=None, description="Date when news was added"
    )
    now_cost: Optional[int] = Field(
        default=None, description="Current cost (in tenths of a million, e.g., 105 = £10.5m)"
    )
    photo: Optional[str] = Field(
        default=None, description="Filename of the player's photo"
    )
    points_per_game: Optional[str] = Field(
        default=None, description="Average points per game"
    )
    second_name: Optional[str] = Field(
        default=None, description="Player's surname"
    )
    selected_by_percent: Optional[str] = Field(
        default=None, description="Percent of managers who own this player"
    )
    special: Optional[bool] = Field(
        default=None, description="Is the player a special (non-standard) player?"
    )
    squad_number: Optional[int] = Field(
        default=None, description="Player's squad number (if available)"
    )
    status: Optional[str] = Field(
        default=None, description="Player's status (e.g., 'a'=available, 'i'=injured, 'd'=doubtful)"
    )
    team: Optional[int] = Field(
        default=None, description="Team ID (see Teams enum)"
    )
    team_code: Optional[int] = Field(
        default=None, description="Unique FPL team code"
    )
    total_points: Optional[int] = Field(
        default=None, description="Total points scored this season"
    )
    transfers_in: Optional[int] = Field(
        default=None, description="Total transfers in this season"
    )
    transfers_in_event: Optional[int] = Field(
        default=None, description="Transfers in this gameweek"
    )
    transfers_out: Optional[int] = Field(
        default=None, description="Total transfers out this season"
    )
    transfers_out_event: Optional[int] = Field(
        default=None, description="Transfers out this gameweek"
    )
    value_form: Optional[str] = Field(
        default=None, description="Value for money based on form"
    )
    value_season: Optional[str] = Field(
        default=None, description="Value for money based on season performance"
    )
    web_name: Optional[str] = Field(
        default=None, description="Player's short web name"
    )
    minutes: Optional[int] = Field(
        default=None, description="Total minutes played this season"
    )
    goals_scored: Optional[int] = Field(
        default=None, description="Total goals scored this season"
    )
    assists: Optional[int] = Field(
        default=None, description="Total assists this season"
    )
    clean_sheets: Optional[int] = Field(
        default=None, description="Total clean sheets this season"
    )
    goals_conceded: Optional[int] = Field(
        default=None, description="Total goals conceded this season"
    )
    own_goals: Optional[int] = Field(
        default=None, description="Total own goals this season"
    )
    penalties_saved: Optional[int] = Field(
        default=None, description="Total penalties saved this season"
    )
    penalties_missed: Optional[int] = Field(
        default=None, description="Total penalties missed this season"
    )
    yellow_cards: Optional[int] = Field(
        default=None, description="Total yellow cards this season"
    )
    red_cards: Optional[int] = Field(
        default=None, description="Total red cards this season"
    )
    saves: Optional[int] = Field(
        default=None, description="Total saves this season (goalkeepers)"
    )
    bonus: Optional[int] = Field(
        default=None, description="Total bonus points awarded this season"
    )
    bps: Optional[int] = Field(
        default=None, description="Total Bonus Points System (BPS) score this season"
    )
    influence: Optional[str] = Field(
        default=None, description="Influence metric (FPL's internal stat)"
    )
    creativity: Optional[str] = Field(
        default=None, description="Creativity metric (FPL's internal stat)"
    )
    threat: Optional[str] = Field(
        default=None, description="Threat metric (FPL's internal stat)"
    )
    ict_index: Optional[str] = Field(
        default=None, description="ICT Index (FPL's internal stat)"
    )
    influence_rank: Optional[int] = Field(
        default=None, description="Rank for influence metric among all players"
    )
    influence_rank_type: Optional[int] = Field(
        default=None, description="Rank for influence metric among players of same position"
    )
    creativity_rank: Optional[int] = Field(
        default=None, description="Rank for creativity metric among all players"
    )
    creativity_rank_type: Optional[int] = Field(
        default=None, description="Rank for creativity metric among players of same position"
    )
    threat_rank: Optional[int] = Field(
        default=None, description="Rank for threat metric among all players"
    )
    threat_rank_type: Optional[int] = Field(
        default=None, description="Rank for threat metric among players of same position"
    )
    ict_index_rank: Optional[int] = Field(
        default=None, description="Rank for ICT Index among all players"
    )
    ict_index_rank_type: Optional[int] = Field(
        default=None, description="Rank for ICT Index among players of same position"
    )

# class Team(BaseModel):
#     team_id: Teams = Field(description="Unique identifier for the team")
#     tean_name: str = Field(description="Name of the team")

class Teams(IntEnum, Enum):
    Arsenal_FC = 1
    Aston_Vill_FC = 2
    Brentford_FC = 3
    Brighton_and_Hove_Albion_FC = 4
    Burnley_FC = 5
    Chelsea_FC = 6
    Crystal_Palace_FC = 7
    Everton_FC = 8
    Leicester_FC = 9
    Leeds_FC = 10
    Liverpool_FC = 11
    Manchester_City_FC = 13
    Manchester_Utd_FC = 12
    Newcastle_FC = 14
    Norwich_FC = 15
    Southampton_FC = 16
    Tottenham_Hotspur_FC = 17
    Watford_FC = 18
    West_Ham_FC = 19
    Wolverhampton_Wanderers_FC = 20


# player = Player(
#     id=1,name="John Doe", position="Forward", team="Team A", points=25.5, status="Active")

# print(player)