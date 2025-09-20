import requests

from domain.constants import BASE_URL, ACCOUNT_HEADERS
from domain.entities.contract import Contract
from domain.interfaces import UseCase


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
                Contract.from_dict(contract_data)
            )

        #
        return contracts


if __name__ == "__main__":
    from pprint import pprint

    contracts = ContractGetter().execute()
    pprint(contracts)
    print(contracts[0].terms.deliver[0].system_symbol)
