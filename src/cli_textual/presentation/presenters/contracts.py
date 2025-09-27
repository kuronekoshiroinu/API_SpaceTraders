from dataclasses import dataclass
import json
from src.traders.domain.entities.contract import Contract


@dataclass
class ContractsPresenter:
    contracts: list[Contract]

    @property
    def to_str(self)-> str:
        tojson = []
        for contract in self.contracts:
            tojson.append(contract.to_dict)
        respuesta=json.dumps(tojson,indent=3)
        return respuesta

