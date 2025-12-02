import datetime as dt

import sqlalchemy as sa

from account.adapters.orm.read_only_models.bank_account_rom import BankAccontROM 
from contract.domain import enums 
from core.base.base_read_only_model import BaseROM 
from core.database import SQLALCHEMY_READONLY_REGISTRY 


class ChequeROM(BaseROM) : 
    id :int 
    payment_id : int 
    serial:str 
    series: str 
    sayaad_code :str 
    image_file_id : int
    category: enums.ChequeCategory 
    payee_type: enums.ChequePayeeType 
    payee_national_code: str 
    status : enums.ChequeStatus
    
    def dumps(self)-> dict: 
        return { 
                'serial':self.serial, 
                'series': self.series , 
                'sayaad_code':self.sayaad_code , 
                'image_file':{'id':str(self.image_file_id)}, 
                'category' : self.category , 
                'payee_type' : self.payee_type , 
                'payee_natioal_code' : self.payee_national_code  , 
                'status' : self.status 
                }
    