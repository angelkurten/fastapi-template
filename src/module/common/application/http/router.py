from fastapi import APIRouter

# Module routers
from .status import router as status_router


def build_router() -> APIRouter:

    router = APIRouter()
    router.include_router(status_router)

    return router
