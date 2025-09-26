from dataclasses import dataclass

from domain.constants import BASE_URL, ACCOUNT_HEADERS, AUTHORIZATION_HEADERS
from domain.interfaces import UseCase
import requests
@dataclass
class ContractAccepter(UseCase):
    contract_id:str

    def execute(self, *args, **kwargs)->str:
        url = f"{BASE_URL}/my/contracts/{self.contract_id}/accept"
        response = requests.post(url,headers=AUTHORIZATION_HEADERS)

        if response.status_code == 200:
            return response.text
        else:
            error_msg = response.json().get('error', {}).get('message', 'Error desconocido')
            raise ValueError(f"Error al aceptar contrato {self.contract_id}: {error_msg}")

if __name__ == "__main__":
    from domain.entities.contract import Contract
    from pprint import pprint
    from infraestructure.services.space_traders_service import SpaceTradersService

    contract:list[Contract] = SpaceTradersService().get_contracts()

    id_contract=contract[0].id
    pprint(contract)
    if contract[0].accepted == False:
        print(type(id_contract))
        accept=ContractAccepter(contract_id=id_contract).execute()
        pprint(accept)