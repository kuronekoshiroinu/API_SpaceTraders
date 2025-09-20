from dataclasses import dataclass
from domain.entities.contract_deliver import ContractDeliver
from domain.entities.contract_payment import ContractPayment

@dataclass
class ContractTerms:
    deadline: str
    deliver: list[ContractDeliver]
    payment: ContractPayment

    @classmethod
    def from_dict(cls, data: dict) :
        return cls(
            deadline=data["deadline"],
            deliver=ContractDeliver.from_list(data["deliver"]),
            payment=ContractPayment.from_dict(data["payment"])
        )
