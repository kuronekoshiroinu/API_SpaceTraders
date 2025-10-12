from dataclasses import dataclass
from wsgiref.util import request_uri


@dataclass
class ContractDeliver:
    destination_symbol: str
    trade_symbol: str
    units_fullfilled: int
    units_required: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            destination_symbol=data["destinationSymbol"],
            trade_symbol=data["tradeSymbol"],
            units_fullfilled=data["unitsFulfilled"],
            units_required=data["unitsRequired"],
        )

    @classmethod
    def from_list(cls, contracts_deliver: list[dict]) -> list["ContractDeliver"]:
        delivers = []
        for contract_deliver in contracts_deliver:
            delivers.append(
                cls.from_dict(contract_deliver)
            )
        return delivers

    @property
    def system_symbol(self) -> str:
        split_destination_symbol = self.destination_symbol.split('-')
        return '-'.join(split_destination_symbol[0:2])


if __name__ == "__main__":
    destination_symbol = 'X1-BF56-H47'
    split_destination_symbol = destination_symbol.split('-')
    print(split_destination_symbol[0:2])
    joiner = '-'.join(split_destination_symbol[0:2])
    print(joiner)
