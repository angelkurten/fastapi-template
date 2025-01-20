from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.module.common.container import CommonContainer


class ModuleContainer(DeclarativeContainer):
    config = providers.Configuration()

    common_container = providers.Container(
        CommonContainer,
        config=config.common,
    )
