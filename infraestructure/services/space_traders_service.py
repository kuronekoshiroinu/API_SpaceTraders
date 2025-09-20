from domain.entities.account import Account
from domain.entities.contract import Contract
from domain.entities.ship_purchase_ship import ShipPurchaseShip
from domain.interfaces import TradersService
import requests
from domain.constants import BASE_URL, AUTHORIZATION_HEADERS, ACCOUNT_HEADERS

class SpaceTradersService(TradersService):
    def get_ships(self, data: list[dict]) -> list[ShipPurchaseShip]:
        response = requests.get(f"{BASE_URL}/my/ships",
                                headers=AUTHORIZATION_HEADERS)
        if response.status_code == 200:
            return ShipPurchaseShip.from_list(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")

    def get_contract(self, data: list[dict]) -> list[Contract]:
        response = requests.get(f"{BASE_URL}/my/contracts", headers=ACCOUNT_HEADERS)

        if response.status_code == 200:
            return Contract.from_list(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener contratos: {response.status_code} - {response.text}")

    def get_account(self, data: dict) -> Account:
        response = requests.get(f"{BASE_URL}/my/agent", headers=ACCOUNT_HEADERS)

        if response.status_code == 200:
            return Account.from_dict(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")


if __name__=="__main__":
    from pprint import pprint
    space=SpaceTradersService()
    #ships=space.get_ships([])
    contract=space.get_contract([])
    account=space.get_account({})
    pprint(account)
