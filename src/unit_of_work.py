from abc import ABC ,abstractmethod

from sqlalchemy import text
from sqlalchemy.orm import Session
from account.adapters import repositories as account_repos
from advertisement.adapters import repositories as ad_repos
from contract.adapters import repositories as contract_repos
from core.base.abstract_unit_of_work import AbstractUnitOfWork
from crm.adapters import repositories as crm_repos
from shared.service_layer.services.storage_servce import StorageService



