from domain.entities.contract import Contract
from domain.entities.contract_deliver import ContractDeliver
from domain.entities.contract_payment import ContractPayment
from domain.entities.contract_terms import ContractTerms
from domain.interfaces import UseCase
import requests
from domain.constants import BASE_URL, ACCOUNT_HEADERS


class ContractGetter(UseCase):
    def execute(self, *args, **kwargs) -> list[Contract]:
        response = requests.get(f"{BASE_URL}/my/contracts", headers=ACCOUNT_HEADERS)

        if response.status_code == 200:
            return self._parse_contracts_data(response.json())
        else:
            raise ValueError(f"Error al obtener contratos: {response.status_code} - {response.text}")

    def _parse_contracts_data(self, api_response: dict) -> list[Contract]:
        """Convierte la respuesta de la API en una lista de objetos Contract"""
        contracts = []
        for contract_data in api_response["data"]:
            contracts.append(
                Contract(
                    id=contract_data["id"],
                    type=contract_data["type"],
                    accepted=contract_data["accepted"],
                    deadline_to_accept=contract_data["deadlineToAccept"],
                    expiration=contract_data["expiration"],
                    faction_symbol=contract_data["factionSymbol"],
                    fulfilled=contract_data["fulfilled"],
                    terms=self._get_contract_terms(contract_data["terms"]),
                )
            )

        #
        return contracts

    @classmethod
    def _get_contract_terms(cls, contract_terms: dict) -> ContractTerms:
        return ContractTerms(
            deadline=contract_terms["deadline"],
            deliver=cls._get_contracts_deliver(contract_terms["deliver"]),
            payment=cls._get_contract_payment(contract_terms["payment"])
        )

    @classmethod
    def _get_contract_payment(cls, contract_payment: dict) -> ContractPayment:
        return ContractPayment(
            on_accepted=contract_payment["onAccepted"],
            on_fulfilled=contract_payment["onFulfilled"],
        )

    @classmethod
    def _get_contracts_deliver(cls, contracts_deliver:list[dict])->list[ContractDeliver]:
        delivers=[]
        for contract_deliver in contracts_deliver:
            delivers.append(
                cls._get_contract_deliver(contract_deliver)
            )
        return delivers

    @classmethod
    def _get_contract_deliver(cls, contract_deliver: dict) -> ContractDeliver:
        return ContractDeliver(
            destination_symbol=contract_deliver["destinationSymbol"],
            trade_symbol=contract_deliver["tradeSymbol"],
            units_fullfilled=contract_deliver["unitsFulfilled"],
            units_required=contract_deliver["unitsRequired"],
        )


if __name__ == "__main__":
    from pprint import pprint
    contracts = ContractGetter().execute()
    pprint(contracts)
    print(contracts[0].terms.deliver[0].system_symbol)
