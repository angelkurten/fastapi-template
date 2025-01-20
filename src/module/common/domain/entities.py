import copy
from dataclasses import dataclass, field
from typing import Any, Self

from src.module.common.domain.values import DateTime


@dataclass(kw_only=True)
class DomainEntity[ID: Any]:
    _id: ID = field()
    _created_at: DateTime = field(default_factory=DateTime.now, kw_only=True)
    _updated_at: DateTime = field(default_factory=DateTime.now, kw_only=True)

    @property
    def id(self) -> ID:
        return self._id

    @property
    def created_at(self) -> DateTime:
        return self._created_at

    @property
    def updated_at(self) -> DateTime:
        return self._updated_at

    def _update(self):
        self._updated_at = DateTime.now()

    def copy(self) -> Self:
        return copy.deepcopy(self)

    def __eq__(self, other):
        if not isinstance(other, DomainEntity):
            raise NotImplementedError()
        return self.id == other.id
