from datetime import datetime

import sqlalchemy as sa

from contract.domain.enums import PRContractStep
from core.base.base_read_only_model import BaseROM
from core.database import SQLALCHEMY_READONLY_REGISTRY


class ContracctStepROM(BaseROM):
    id: int
    contract_id: int
    type: PRContractStep
    completed_at: datetime | None
    deleted_at: datetime | None

    def dumps(self) -> dict:
        return {"type": self.type, "completed_at": self.completed_at}


contract_step_rom = sa.Table(
    "contract_steps",
    SQLALCHEMY_READONLY_REGISTRY.metadata,
    sa.Column("id", sa.BigInteger, primary_key=True),
    sa.Column(
        "contract_id",
        sa.BigInteger,
        sa.ForeignKey("contract.contracts.id"),
        nullable=False,
    ),
    sa.Column("type", sa.String, nullable=False),
    sa.Column("completed_at", sa.DateTime),
    sa.Column("deleted_at", sa.DateTime),
    schema="contract",
)
