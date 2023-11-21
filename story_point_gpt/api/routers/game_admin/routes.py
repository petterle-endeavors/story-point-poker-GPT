from fastapi import APIRouter, Request, Body, Query
from .schemas import (
    StartGameRequest,
    StartGameResponse,
    JoinGameRequest,
    JoinGameResponse,
    EndGameRequest,
    EndGameResponse,
    VotingStatusResponse,
    ResultsResponse
)


ROUTER = APIRouter()


@ROUTER.post(
    "/start-game",
    name="Start a new game",
    operation_id="start_game",
    description="Starts a new game session, optionally with an admin code.",
    response_model=StartGameResponse
)
def start_game(
    start_request: StartGameRequest = Body(...),
    request: Request
) -> StartGameResponse:
    """Start a new game session."""
    # Your logic here to start a new game
    # ...

    return StartGameResponse(
        game_code="unique-game-code",
        confirmation="Game has started successfully.",
        session_identifier="session-identifier"
    )

@ROUTER.post(
    "/join-game",
    name="Join an existing game",
    operation_id="join_game",
    description="Allows a player to join a game using the game code.",
    response_model=JoinGameResponse
)
def join_game(
    join_request: JoinGameRequest = Body(...),
    request: Request
) -> JoinGameResponse:
    """Join an existing game."""
    # Your logic here to join a game
    # ...

    return JoinGameResponse(
        confirmation="Player has joined the game successfully.",
        player_identifier="unique-player-identifier"
    )

@ROUTER.post(
    "/end-game",
    name="End the game session",
    operation_id="end_game",
    description="Ends the game session using the admin code.",
    response_model=EndGameResponse
)
def end_game(
    end_request: EndGameRequest = Body(...),
    request: Request
) -> EndGameResponse:
    """End the game session."""
    # Your logic here to end the game
    # ...

    return EndGameResponse(
        confirmation="Game has ended successfully."
    )

@ROUTER.get(
    "/has-everyone-voted",
    name="Check if all players have voted",
    operation_id="has_everyone_voted",
    description="Checks if all players in the game have cast their votes.",
    response_model=VotingStatusResponse
)
def has_everyone_voted(
    game_code: str = Query(..., description="The game code to check voting status."),
    session_identifier: Optional[str] = Query(None, description="Optional session identifier."),
    request: Request
) -> VotingStatusResponse:
    """Check if all players have voted."""
    # Your logic here to check voting status
    # ...

    return VotingStatusResponse(
        has_everyone_voted=True,
        details=None  # Fill with details if necessary
    )

@ROUTER.get(
    "/results",
    name="Get voting results",
    operation_id="get_voting_results",
    description="Gathers and returns the results from the voting round.",
    response_model=ResultsResponse
)
def get_results(
    game_code: str = Query(..., description="The game code to get results for."),
    session_identifier: Optional[str] = Query(None, description="Optional session identifier."),
    request: Request
) -> ResultsResponse:
    """Get the results of the voting."""
    # Your logic here to calculate and retrieve results
    # ...

    return ResultsResponse(
        votes=[{"player_identifier": "player1", "vote": "optionA"}, {"player_identifier": "player2", "vote": "optionB"}],
        results={"winner": "optionA"}
    )