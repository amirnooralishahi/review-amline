from datetime import date as _date
from datetime import datetime

import sqlalchemy as sa

from account.adapters.orm.read_only_models import BankAccountROM
from contract.adapters.orm.read_only_models.contract_rom import ContractROM
from contract.domain.enums import PartyType, PRContractState, TrackingCodeStatus
from core.base.base_read_only_model import BaseROM
from shared.adapters.orm.read_only_models import PropertyROM


class PRContractROM(BaseROM) :
    id:int
    property:PropertyROM 
    property_id :int
    contract:ContractROM 
    contract_id:int
    
    property_handover_date:_date | None 
    date: _date | None 
    start_date : _date | None 
    end_date: _date  | None 
    deposit_amount : int | None 
    rent_amount : int | None 
    
    renant_bank_account : BankAccountROM | NOne