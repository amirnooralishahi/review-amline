from account.domain.entities.user import User
from contract.domain.entities.contract_party import ContractParty
from contract.domain.entities.contract_step import ContractStep
from contract.domain.entities.property_rent_contract import PropertyRentContract
from contract.domain.enums import (
    ContractStatus,
    PartyType,
    PRContractState,
    PRContractStep,
)
from contract.domain.prcontract.prcontract_step_manager import PRContractStepManager
from contract.domain.types import ContractOwner
from contract.service_layer.exceptions import UserIsNotContractPartyException
from core.translates import perm_trans 
from core.translates.conflict_exception import ConflictExcTrans 


class  PRContractService :
    def __init__(self,step_manager :PRContractStepManager= PRContractStepManager()): 
        self.step_manager = step_manager 
    
    def get_contract_state( 
        sel):pass 
