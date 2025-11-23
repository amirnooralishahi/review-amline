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


class Otp(NamedTuple):
    type: OtpType
    key: str
    value: str

    @property
    def msg(self) -> str:
        return f'{self.type.value}: {self.value}'


class JWTConfig(NamedTuple):
    secret_key: str
    access_expire: int
    refresh_expire: int
    algorithm: str


class MinioConfig(NamedTuple):
    endpoint: str
    access_key: str
    secret_key: str
    private_bucket: str
    public_bucket: str
    url_expire_minutes: int


class RedisConfig(NamedTuple):
    host: str
    port: int
    password: str
    db: int


class ElasticSearchConfig(NamedTuple):
    host: str
    port: int
    password: str


class KaveNegarConfig(NamedTuple):
    api_key: str


class TSMConfig(NamedTuple):
    username: str
    password: str
    sender_number: str
    ding_sender_numer: str


class SMSTemplates(NamedTuple):
    otp_template: str
    sign_contact_otp_template: str
    invitation_to_landlord_template: str
    invitation_to_tenant_template: str
    counter_party_signed_template: str
    counter_party_rejected_template: str
    edite_requested_template: str
    custom_payment_template: str
    wallet_charge_template: str
    invoice_link_template: str


class KenarDivarURLs(NamedTuple):
    post_info: str
    user_token: str
    user_info: str


class BaleURLs(NamedTuple):
    authH_token: str
    send_otp: str


class TsmsURLs(NamedTuple):
    send_message: str


class AmlineURLs(NamedTuple):
    production_api: str
    staging_api: str
    production_frontend: str
    staging_frontend: str
    contract_payments: str
    contract: str


class TelegramURLs(NamedTuple):
    send_message: str


@dataclass
class FinnotechConfig:
    uri: str
    client_id: str
    secret: str
    national_code: str
    scopes: str
