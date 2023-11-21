from pydantic import Field
from typing import Optional, List
from ..shared import BaseAPIModel, to_camel_case


# Model for the start-game endpoint
class StartGameRequest(BaseAPIModel):
    admin_code: Optional[str] = Field(
        None,
        description="An optional 4-digit admin code to authorize the start of a new game session.",
    )


class StartGameResponse(BaseAPIModel):
    game_code: str = Field(
        ...,
        description="A unique game code for the session.",
    )
    confirmation: str = Field(
        ...,
        description="Confirmation message of the game start.",
    )
    session_identifier: Optional[str] = Field(
        None,
        description="An optional session identifier for the game session.",
    )

# Model for the join-game endpoint
class JoinGameRequest(BaseAPIModel):
    game_code: str = Field(
        ...,
        description="The unique game code to join a game session.",
    )


class JoinGameResponse(BaseAPIModel):
    confirmation: str = Field(
        ...,
        description="Confirmation message of joining the game.",
    )
    player_identifier: str = Field(
        ...,
        description="A unique identifier for the player who just joined.",
    )

# Model for the end-game endpoint
class EndGameRequest(BaseAPIModel):
    admin_code: str = Field(
        ...,
        description="The 4-digit admin code to authenticate the request to end the game session.",
    )
    game_code: str = Field(
        ...,
        description="The game code of the session to end.",
    )


class EndGameResponse(BaseAPIModel):
    confirmation: str = Field(
        ...,
        description="Confirmation message that the game session has ended.",
    )

# Since has-everyone-voted is a GET endpoint, it usually won't need a request model.
# If input is passed as query parameters, there's no need for a request body model.

class VotingStatusResponse(BaseAPIModel):
    has_everyone_voted: bool = Field(
        ...,
        description="Indicates whether all players have cast their votes or not.",
    )
    # Optionally, include detailed status
    details: Optional[List[str]] = Field(
        None,
        description="Detailed information about which players have or have not voted.",
    )

# The results GET endpoint might not need a request model, depending on how you're passing inputs.
# But here's a response model.
class ResultsResponse(BaseAPIModel):
    votes: List[dict] = Field(
        ...,
        description="The list of votes received during the round.",
    )
    results: dict = Field(
        ...,
        description="Any calculated results for the round.",
    )