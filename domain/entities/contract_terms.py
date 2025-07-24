from dataclasses import dataclass
from domain.entities.contract_deliver import ContractDeliver
from domain.entities.contract_payment import ContractPayment

@dataclass
class ContractTerms:
    deadline: str
    deliver: list[ContractDeliver]
    payment: ContractPayment