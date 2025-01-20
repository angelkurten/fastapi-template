from datetime import UTC, datetime
from typing import Self


class DateTime(datetime):

    @classmethod
    # pylint: disable=W0221
    def now(cls) -> Self:
        return super(DateTime, cls).now(UTC)
