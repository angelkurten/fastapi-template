from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.app.fast_api import build_fastapi, build_router
from src.app.logger import configure_logger
from src.app.utils import find_providers
from src.config.app import AppConfig
from src.module.container import ModuleContainer
from src.module.providers import RouteProvider


class MainContainer(DeclarativeContainer):
    config = providers.Configuration()

    __self__ = providers.Self()

    logger = providers.Resource(
        configure_logger,
        log_level=config.log_level,
    )

    app_config = providers.Factory(
        AppConfig,
        name=config.name,
        profiles=config.profiles,
        debug=config.debug,
    )

    module_container = providers.Container(
        ModuleContainer,
        config=config.module,
    )

    fastapi = providers.Singleton(
        build_fastapi,
        router=providers.Singleton(
            build_router,
            providers.Factory(find_providers, __self__, RouteProvider),
        ),
        app_config=app_config,
    )
