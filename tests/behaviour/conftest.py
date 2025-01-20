import pytest

from src.app.application import Application


@pytest.fixture(scope="function")
def application():

    # Override in runtime the configuration
    config = {}

    app = Application(config, "./config/test.yaml")
    app.init()

    yield app

    print(f"Used Application::Config - {app.container.config}")

    app.shutdown()

    # Clear the Singleton instance for the next execution
    Application.remove_instance()
