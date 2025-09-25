import requests

#from aplication.use_cases.ship_available_viewer import ShipAvailableViewer
from domain.constants import BASE_URL, AUTHORIZATION_HEADERS, ACCOUNT_HEADERS
from domain.entities.account import Account
from domain.entities.contract import Contract
from domain.entities.engineered_asteroid import EngineeredAsteroid
from domain.entities.ship_purchase_ship import ShipPurchaseShip
from domain.entities.ships_available import ShipsAvailable
from domain.entities.shipyard import Shipyard
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

    def find_engineered_asteroids(self, system_symbol:str) -> list[EngineeredAsteroid]:
        return EngineeredAsteroid.from_list(
            asteroids_data=self._get_endpoint_response(
                endpoint=f"systems/{system_symbol}/waypoints?type=ENGINEERED_ASTEROID",
                headers=ACCOUNT_HEADERS,
            )
        )

    def find_shipyards(self, system_symbol:str) -> list[Shipyard]:
        return Shipyard.from_list(
            shipyards_data_list=self._get_endpoint_response(
                endpoint=f"/systems/{system_symbol}/waypoints?traits=SHIPYARD",
                headers=AUTHORIZATION_HEADERS,
            )
        )

    def view_ship_available(self, system_symbol:str, waypoint_symbol:str) -> ShipsAvailable:
        return ShipsAvailable.from_dict(
            data=self._get_endpoint_response(
                endpoint=f"/systems/{system_symbol}/waypoints/{waypoint_symbol}/shipyard",
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
    from aplication.use_cases.shipyard_finder import ShipyardFinder
    from domain.entities.ships_available import ShipsAvailable
    space = SpaceTradersService()
    ships=space.get_ships()
    contract = space.get_contract()
    account = space.get_account()
    #asteroids=space.find_engineered_asteroids(contract[0].terms.deliver[0].system_symbol)
    shipyards_infos=space.find_shipyards(system_symbol=contract[0].terms.deliver[0].system_symbol)
    available_ships_info=space.view_ship_available(system_symbol=contract[0].terms.deliver[0].system_symbol,
                                                   waypoint_symbol=shipyards_infos[2].symbol)
    pprint(available_ships_info)
    #pprint(shipyards_infos)
