from dataclasses import dataclass, asdict
from typing import Protocol, Type, TypedDict
from sqlalchemy import Column
from typing_extensions import NamedTuple
from account.domain.enums import UserRole
from core.base.base_dto import BaseDto
from core.enums import SortDirection
from core.excepions import ValidationException
from core.translates import validation_trans
from shared.domain.enums import OtpType


@dataclass
class OperationResult:
    message: str
    success: bool = True

    @classmethod
    def ok(cls, message: str) -> 'OperationResult':
        return cls(success=True, message=message)


@dataclass
class PaginatedList:
    total_count: int
    start_index: int
    end_index: int
    data: list[dict]


@dataclass
class PaginateParams:
    offset: int = 0
    limit: int = 50
    sort_direction: SortDirection = SortDirection.ASC
    sort_by: str = 'created_at'

    def dumps(self) -> dict:
        return asdict(self)

    def get_order(self, entity_type: Type):
        """
        Build order clause based on the sort direction and sort by field.
        """
        order_field: Column | None = getattr(entity_type, self.sort_by, None) or getattr(entity_type, "id", None)
        if order_field is None:
            raise ValidationException(
                detail=validation_trans.invalid_sort_field,
            )

        if self.sort_direction == 'asc':
            return order_field.asc()

        elif self.sort_direction == 'desc':
            return order_field.desc()

        else:
            raise ValidationException(
                detail=validation_trans.invalid_sort_field,
                context={'entity': entity_type.__name__, "sort_direction": self.sort_direction},
            )


class FilterCriteria(TypedDict):
    field_names: set[str]
    value: str | int


class CurrentUser(Protocol):
    id: int
    mobile: str
    first_name: str | None
    last_name: str | None
    nick_name: str | None
    national_code: str | None
    roles: list[UserRole]
    is_active: bool

    # ????
    @property
    def is_admin(self) -> bool: ...


@dataclass
class FileDto(BaseDto):
    id: int
    url: str | None = None

    def dumps(self) -> dict:
        return {"id": str(self.id), "url": self.url}
