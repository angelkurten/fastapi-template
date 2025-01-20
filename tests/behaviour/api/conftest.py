import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def client(application) -> TestClient:
    return TestClient(application.fastapi())
