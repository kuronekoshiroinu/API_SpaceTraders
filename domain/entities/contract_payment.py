from dataclasses import dataclass
@dataclass
class ContractPayment:
    on_accepted: int
    on_fulfilled:int