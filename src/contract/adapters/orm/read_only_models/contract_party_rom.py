from datetime import datetime 

import sqlalchemy as sa

from account.adapters.orm.read_only_models import UserROM 
from contract.domain.enums import PartyType 
from core.base.base_read_only_model import BaseROM

class ContractPartyROM(BaseROM) : 
    id : int 
    contract_id : int
    user_id: int
    user:UserROM 
    party_type : PartyType 
    deleted_at : datetime | None 
    
    
    def dumps(self) -> dict  : 
        return { 
            'id':str(self.id), 
            'party_type' : self.party_type , 
            'user' : self.user.dumps()
            }