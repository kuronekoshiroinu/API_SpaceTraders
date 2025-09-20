from dataclasses import dataclass
@dataclass
class ContractPayment:
    on_accepted: int
    on_fulfilled:int

    @classmethod
    def from_dict(cls, data: dict) :
        return cls(
            on_accepted=data["onAccepted"],
            on_fulfilled=data["onFulfilled"],
        )