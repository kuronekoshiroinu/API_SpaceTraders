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

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            id=data["id"],
            type=data["type"],
            accepted=data["accepted"],
            deadline_to_accept=data["deadlineToAccept"],
            expiration=data["expiration"],
            faction_symbol=data["factionSymbol"],
            fulfilled=data["fulfilled"],
            terms=ContractTerms.from_dict(data["terms"]),
        )
