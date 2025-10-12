from dataclasses import dataclass, asdict
from src.traders.domain.entities.contract_terms import ContractTerms


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
    def from_dict(cls, data: dict):
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

    @classmethod
    def from_list(cls, contracts_list: list[dict]) -> list["Contract"]:
        contracts = []
        for contract_dict in contracts_list:
            contracts.append(
                cls.from_dict(contract_dict)
            )
        return contracts

    @property
    def to_dict(self) -> dict:
        return asdict(self)
