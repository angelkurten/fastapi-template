from abc import abstractmethod
from datetime import datetime
from logging import getLogger

from pydantic import BaseModel, ConfigDict

_logger = getLogger(__name__)


class UseCaseRequest(BaseModel):
    model_config = ConfigDict(frozen=True)


class UseCaseResponse(BaseModel):
    model_config = ConfigDict(frozen=True)


class UseCase[Request: UseCaseRequest, Response: UseCaseResponse]:

    async def __call__(self, request: Request) -> Response:
        start = datetime.now()

        _logger.debug("Execute UseCase[%s] with %s", self.__class__.__name__, request)

        result = await self.execute(request)

        _logger.debug(
            "Finish UseCase[%s] on time {%s} with %s",
            self.__class__.__name__,
            datetime.now() - start,
            result,
        )

        return result

    @abstractmethod
    async def execute(self, request: Request) -> Response:
        """
        Implements the UseCase Logic
        """
