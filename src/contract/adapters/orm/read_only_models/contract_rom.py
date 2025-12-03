from datetime import datetime 
from datetime import date as _date 

import sqlalchemy as sa
from account.adapters.orm.read_only_models.bank_account_rom import BankAccountROM
from contract.adapters.orm.read_only_models.contract_clause_rom import ConractClausesROM 
from contract.adapters.orm.read_only_models.contract_party_rom import ContractPartyROM 
from contract.adapters.orm.read_only_models.contract_payments_roms import ContractPaymentROM 
from contract.adapters.orm.read_only_models.contract_step_rom import Contract