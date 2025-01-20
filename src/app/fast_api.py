from typing import Callable, List

from fastapi import APIRouter, FastAPI

from src.config.app import AppConfig


def build_router(routes: List[APIRouter]) -> APIRouter:
    router = APIRouter()

    for route in routes:
        router.include_router(route)

    return router


def build_fastapi(
    router: APIRouter, app_config: AppConfig, lifespan: Callable
) -> FastAPI:

    api = FastAPI(
        name=app_config.name,
        debug=app_config.debug,
        lifespan=lifespan,
    )

    api.include_router(router)

    return api
