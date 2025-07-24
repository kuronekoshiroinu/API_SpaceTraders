from dataclasses import dataclass
from domain.entities.contract_terms import ContractTerms

@dataclass
class Contract:
    id: str
    type: str
    accepted: bool
    deadline_to_accept: str
    expiration: str
    faction_symbol: str
    fulfilled: bool
    terms: ContractTerms
