from typing import Generator
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from account.domain.entities import User
from account.domain.enums import UserRole
from account.service_layer.services.token_service import JwTokenService, TokenService
from contract.domain.prcontract import (
    MonthlyRentservice,
    PRcContractCommissionServce,
    PRcountractService,
)
from contract.domain.prcontract.prcontract_pdf_generato_service import (
    PRContractPDFGeneratorService,
    PRContractPDFGeneratorServiceImpl,

)
