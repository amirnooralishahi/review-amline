from typing import Generator
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from src.account.domain.entities.user import User
from src.account.domain.enums import UserRole
from src.account.service_layer.services.token_service import JwTokenService, TokenService
from src.contract.domain.prcontract import (
    MonthlyRentservice,
    PRcContractCommissionServce,
    PRcountractService,
)
from src.contract.domain.prcontract.prcontract_pdf_generator_service import (
    PRContractPDFGeneratorService,
    PRContractPDFGeneratorServiceImpl,

)
