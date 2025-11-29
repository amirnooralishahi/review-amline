from abc import ABC , abstractmethod 
from datetime import date,datetime
from typing import TypeDict

import pytz 
import requests 

from core.excepions import NotFoundException,ProcessingException
from core.logger import Logger 
from core.translates.not_found_exception import NotFoundExcTrans 
from core.translates.processing_exception import ProcessingExcTrans 
from unit_of_work import UnitOfWork 

logger= Logger('pdf--generator-service')

tehran_time_zone = pytz.timezone('Asia/Tegran') 

class BankAccount(TypeDict) : 
    id :int
    iban:str
    owner_name:str 


class BankAccounts(TypeDict): 
    tenant_ba : BankAccount 
    landlord_rent_ba : BankAccount 
    landlord_deposit_ba: BankAccount 


class Tenant(TypeDict): 
    user_id : int
    mobile: str 
    first_name : str 
    last_name: str 
    father_name: str 
    national_code : str 
    address: str 
    signed_at : datetime
    bank_account:BankAccount 
    birth_date:str|  None 

class Landlord(TypeDict) : 
    user_id : int
    mobile : str  
    first_name:str 
    last_name: str
    father_name: str 
    national_code: str 
    address:str 
    signed_at: datetime 
    rent_bank_account : BankAccount 
    deposit_bank_account :  BankAccount 
    birth_date:str | None 


class Clause(TypeDict): 
    clause_name :str 
    clause_number: int  
    subclause_number: int #what
    subclause_name : str | None #what
    body:str 

class Cheque(TypeDict) : 
    serial:str 
    series: str 
    sayaad_code :str 
    category:str 
    payee_type :str 
    payee_national_code :str 

class Payment(TypeDict) : 
    amount: int
    due_date: date
    is_bulk: bool 
    description : str | None  
    method : str 
    type: str 
    cheque: Cheque | None 

class property(TypeDict) : 
    property_type : str 
    deed_status : str
    address: str 
    city:dict 
    electricity_bill_id : str | None
    postal_code  : str  |None 
    registration_area : str  | None 
    main_register_number  : int | None 
    sub_register_number : int | None 
    
    
    area: float | None 
    build_year: int | None 
    structure_type : str 
    facade_types : list[str] 
    direction_type :str 
    flooring_types :list [str] 
    is_rebild : bool | None 
     