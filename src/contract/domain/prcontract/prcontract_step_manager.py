from contract.domain.enums import (
    ContractStatus,
    PartyType,
    PRContractState,
    PRContractStep,
)


class PRContractStepManager:
    def get_contract_state(
        self,
        completed_steps: list | set,
        status: ContractStatus,
        owner_party_type: PartyType,
    ) -> PRContractState:
        if status == ContractStatus.ADMIN_REJECTED:
            return PRContractState.ADMIN_REJECTED
        if (
            status == ContractStatus.PARTY_REJECTED
            and owner_party_type == PartyType.TENANT
        ):
            return PRContractState.LANDLORD_REJECTED
        if (
            status == ContractStatus.PARTY_REJECTED
            and owner_party_type == PartyType.LANDLORD
        ):
            return PRContractState.LANDLORD_REJECTED

        if (
            status == ContractStatus.EDIT_REQUESTED
            and owner_party_type == PartyType.TENANT
        ):
            return PRContractState.LANDLORD_EDIT_REQEUEST
        if (
            status == ContractStatus.EDIT_REQUESTED
            and owner_party_type == PartyType.LANDLORD
        ):
            return PRContractState.TENANT_EDIT_REQUEST

        steps_types = {PRContractStep.resolve(step) for step in completed_steps}

        if self.tracking_code_delivered_steps.issubset(steps_types):
            return PRContractState.TRACKING_CODE_DELIVERED 
        if self.tracking_code_requested_steps.issubset(steps_types): 
            return PRContractState.PENDING_TRACKING_CODE_DELIVERY 
        if self.admin_approved_steps.issubset(steps_types): 
            return PRContractState.PENDING_TRACKING_CODE_REQUEST 
        if self.required_steps_for_admin_approve.issubset(steps_types): 
            return PRContractState.PENDING_ADMIN_APPROVAL 
        if self.tenant_payed_commission_steps.issubset(steps_types): 
            return PRContractState.PENDING_LANDLORD_COMMISSION 
        if self.landlord_payed_commission_steps.issubset(steps_types): 
            return PRContractState.PENDING_TENANT_COMMISSION 
        if self.tenant_signed_steps_tenant_owner.issubset(steps_types): 
            return PRContractState.PENDING_PAYING_COMMISSION 
        
        
        if owner_party_type == PartyType.TENANT: 
            if self.required_steps_for_tenant_signature_tenant_ownerx.issubset(steps_types): 
                return PRContractState.PENDING_TENANT_SIGNATURE 
            if self.required_steps_for_tenant_signature_landlord_ownerx.issubset(steps_types): 
                return PRContractState.PENDING_LANDLORD_SIGNATURE 
            
    @property 
    def landlord_payed_commission_steps(self)->set[PRContractStep]: 
        return self.required_steps_for_paying_commission | {PRContractStep.LANDLORD_COMMISSION}
    
    
    @property 
    def tenant_payed_commission_steps(self)->set[PRContractStep]: 
        return self.required_steps_for_paying_commission | {PRContractStep.TENANT_COMMISSION}
    
    @property 
    def tracking_code_requested_steps(self)->set[PRContractStep]: 
        return self.required_steps_for_requesting_tracking_code | {PRContractStep.TRACKING_CODE_REQUESTED}
    @property
    def tracking_code_delivered_steps(self) -> set[PRContractStep]:
        return self.required_steps_for_delivering_tracking | {
            PRContractStep.TRACKING_CODE_DELIVERED
        }

    @property
    def required_steps_for_delivering_tracking_code(self) -> set[PRContractStep]:
        return self.tracking_code_requested_steps

    @property
    def traking_code_requested_steps(self) -> set[PRContractStep]:
        return self.required_steps_for_requesting_tracking_code | {
            PRContractStep.TRACKING_CODE_REQUESTED
        }

    @property
    def required_steps_for_requesting_tracking_code(self) -> set[PRContractStep]:
        return self.admin_approved_steps

    @property 
    def required_steps_for_paying_commission(self)->set[PRContractStep]: 
        return self.tenant_signed_steps_landlord_owner
    
    @property
    def required_steps_for_admin_approve(self):
        return self.required_steps_for_paying_commission | {
            PRContractStep.LANDLORD_COMMISSION,
            PRContractStep.TENANT_COMMISSION,
        }

    @property
    def admin_approved_steps(self) -> set[PRContractStep]:
        return self.required_steps_for_admin_approve | {PRContractStep.ADMIN_APPROVE}

    @property
    def required_stps_for_admin_approve(self) -> set[PRContractStep]:
        return self.required_steps_for_paying_commission | {
            PRContractStep.LANDLORD_COMMISSION,
            PRContractStep.TENANT_COMMISSION,
        }

    @property
    def required_steps_for_paying_commission(self) -> set[PRContractStep]:
        return self.tenant_signed_steps_landlord_owner

    @property
    def tenant_signed_steps_landlord_owner(self) -> set[PRContractStep]:
        return self.required_steps_for_tenant_signature_landlord_owner | {
            PRContractStep.TENANT_SIGNATURE
        }

    @property
    def required_steps_for_tenant_signature_landlord_owner(self) -> set[PRContractStep]:
        return self.landlord_signed_steps_landlord_owner | {
            PRContractStep.TENANT_INFORMATION
        }

    @property
    def landlord_signed_steps_landlord_owner(self) -> set[PRContractStep]:
        return self.required_steps_for_landlord_signature_landlord_owner | {
            PRContractStep.LANDLORD_SIGNATURE
        }
