from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.module.common.application.http import build_router
from src.module.providers import RouteProvider


class CommonContainer(DeclarativeContainer):
    config = providers.Configuration()

    routes = RouteProvider(build_router)
