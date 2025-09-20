import requests

from domain.constants import BASE_URL, AUTHORIZATION_HEADERS, ACCOUNT_HEADERS
from domain.entities.account import Account
from domain.entities.contract import Contract
from domain.entities.ship_purchase_ship import ShipPurchaseShip
from domain.interfaces import TradersService


class SpaceTradersService(TradersService):
    def get_ships(self) -> list[ShipPurchaseShip]:
        return ShipPurchaseShip.from_list(
            data=self._get_endpoint_response(
                endpoint="/my/ships",
                headers=AUTHORIZATION_HEADERS,
            )
        )

    def get_contract(self) -> list[Contract]:
        return Contract.from_list(
            contracts_list=self._get_endpoint_response(
                endpoint="/my/contracts",
                headers=ACCOUNT_HEADERS,
            )
        )

    def get_account(self) -> Account:
        return Account.from_dict(
            data=self._get_endpoint_response(
                endpoint="/my/agent",
                headers=ACCOUNT_HEADERS,
            )
        )

    @classmethod
    def _get_endpoint_response(cls, endpoint: str, headers: dict):
        response = requests.get(f"{BASE_URL}{endpoint}",
                                headers=headers)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")


if __name__ == "__main__":
    from pprint import pprint

    space = SpaceTradersService()
    ships=space.get_ships()
    contract = space.get_contract()
    account = space.get_account()
    pprint(ships)
