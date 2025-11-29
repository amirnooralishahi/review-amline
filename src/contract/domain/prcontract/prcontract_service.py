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
from core.excepions import ConflictException ,PermissionException
from core.translates import perm_trans
from core.translates.conflict_exception import ConflictExcTrans


class PRContractService:
    def __init__(self, step_manager: PRContractStepManager = PRContractStepManager()):
        self.step_manager = step_manager

    def get_contract_state(
        self,
        completed_steps: list | set,
        contract_status: ContractStatus,
        owner_party_type: PartyType,
    ) -> PRContractState:
        return self.step_manager.get_contract_state(
            completed_steps, contract_status, owner_party_type
        )

    def validate_party_hs_permission_for_step(
        self,
        prc: PropertyRentContract,
        party: ContractParty,
        step: PRContractStep,
        completed_steps: list[ContractStep] = list(),
    ) -> None:

        if prc.statusin [ContractStatus.ADMIN_REJECTED,ContractStatus.PARTY_REJECTED,ContractStatus.EDIT_REQUESTED]: 
            raise PermissionException( 
                                      perm_trans.contract_is_not_editable , 
                                      context={'message': f'contract is in {prc.status} state'})
        
        if prc.status == ContractStatus.DRAFT  and prc.owner_user_id !=party.user_id  :
            raise PermissionException(perm_trans.party_is_not_contract_owner)

        stpes_types= {PRContractStep.resolve(step.type) for step in completed_steps}
        
        if step in [PRContractStep.LANDLORD_REJECTED,PRContractStep.TENANTE_REJECTED] : 
            if prc.owner.user_id == party.user_id : 
                