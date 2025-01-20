import os
from typing import Type

from fastapi import FastAPI

from src.app.container import MainContainer
from src.app.utils import Singleton
from src.module.providers import UseCaseProvider


class Application(metaclass=Singleton):

    container: MainContainer

    @classmethod
    def remove_instance(cls):
        Singleton.remove_instance(cls)

    def __init__(self, config=None, config_path=None):
        if config is None:
            config = {}

        if config_path is None:
            config_path = os.environ.get(
                "APP_CONFIGURATION_FILE", default="./config/development.yaml"
            )

        self.container = MainContainer()
        self.container.config.from_yaml(config_path, required=True)
        self.container.config.from_dict(config)

        if self.container.config.debug():
            self.container.check_dependencies()

    def init(self):
        self.container.init_resources()

    def shutdown(self):
        self.container.shutdown_resources()

    def fastapi(self, lifespan=None) -> FastAPI:
        return self.container.fastapi(lifespan=lifespan)

    def find_use_case[UseCase](self, uc_type: Type[UseCase]) -> UseCase:
        providers = list(self.container.traverse(types=[UseCaseProvider]))

        for provider in providers:
            if provider.cls == uc_type:
                return provider()

        raise KeyError(f"No UseCase found for {uc_type}")
