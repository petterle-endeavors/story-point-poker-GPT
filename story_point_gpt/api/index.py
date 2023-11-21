"""Define the main entry point for the API."""
from fastapi import FastAPI
from mangum import Mangum

from story_point_gpt.api.routers.admin.routes import ROUTER as health_router
from story_point_gpt.api.routers.game_admin.routes import ROUTER as game_admin_router
from story_point_gpt.api.settings import (
    Settings,
    RUNTIME_SETTINGS_ATTRIBUTE_NAME,
)


APP = FastAPI(
    title="Story Point Poker GPT",
    description="A GPT that hosts a story point poker game.",
    version="0.0.0",
)
setattr(APP.state, RUNTIME_SETTINGS_ATTRIBUTE_NAME, Settings())
APP.include_router(health_router, prefix="/admin", tags=["admin"])
APP.include_router(game_admin_router, prefix="/game-admin", tags=["game-admin"])


handler = Mangum(APP)
