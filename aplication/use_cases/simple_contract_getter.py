from dataclasses import dataclass

from domain.entities.contract import Contract
from domain.entities.contract_deliver import ContractDeliver
from domain.interfaces import UseCase, TradersService


@dataclass
class SimpleContractGetter(UseCase):
    trader_service: TradersService

    def execute(self, *args, **kwargs) -> dict:
        contracts = self.trader_service.get_contracts()
        contract = self._get_first_contract(contracts=contracts)
        delivers=contract.terms.deliver
        deliver=self._get_first_deliver(delivers=delivers)
        tipo = contract.type
        system_symbol = deliver.system_symbol
        full = contract.fulfilled
        return {"tipo de contrato": tipo,
                "simbolo del sistema": system_symbol,
                "completado": full}

    def _get_first_contract(self, contracts: list[Contract]) -> Contract:
        return contracts[0]

    def _get_first_deliver(self, delivers: list[ContractDeliver])-> ContractDeliver:
        return delivers[0]