from dataclasses import dataclass
@dataclass
class ContractDeliver:
    destination_symbol: str
    trade_symbol: str
    units_fullfilled: int
    units_required: int