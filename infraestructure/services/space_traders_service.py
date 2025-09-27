from zoneinfo import available_timezones

import requests

# from aplication.use_cases.ship_available_viewer import ShipAvailableViewer
from domain.constants import BASE_URL, AUTHORIZATION_HEADERS, ACCOUNT_HEADERS
from domain.entities.account import Account
from domain.entities.contract import Contract
from domain.entities.engineered_asteroid import EngineeredAsteroid
from domain.entities.ship_purchase import ShipPurchase
from domain.entities.ship_purchase_ship import ShipPurchaseShip
from domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from domain.entities.ship_refuel import ShipRefuel
from domain.entities.ships_available import ShipsAvailable
from domain.entities.shipyard import Shipyard
from domain.entities.to_asteroid_navigate import ToAsteroidNavigate
from domain.interfaces import TradersService


class SpaceTradersService(TradersService):
    def get_ships(self) -> list[ShipPurchaseShip]:
        return ShipPurchaseShip.from_list(
            data=self._get_endpoint_response(
                endpoint="/my/ships",
                headers=AUTHORIZATION_HEADERS,
            )
        )

    def get_contracts(self) -> list[Contract]:
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

    def find_engineered_asteroids(self, system_symbol: str) -> list[EngineeredAsteroid]:
        return EngineeredAsteroid.from_list(
            asteroids_data=self._get_endpoint_response(
                endpoint=f"systems/{system_symbol}/waypoints?type=ENGINEERED_ASTEROID",
                headers=ACCOUNT_HEADERS,
            )
        )

    def find_shipyards(self, system_symbol: str) -> list[Shipyard]:
        return Shipyard.from_list(
            shipyards_data_list=self._get_endpoint_response(
                endpoint=f"/systems/{system_symbol}/waypoints?traits=SHIPYARD",
                headers=AUTHORIZATION_HEADERS,
            )
        )

    def view_ship_available(self, system_symbol: str, waypoint_symbol: str) -> ShipsAvailable:
        return ShipsAvailable.from_dict(
            data=self._get_endpoint_response(
                endpoint=f"/systems/{system_symbol}/waypoints/{waypoint_symbol}/shipyard",
                headers=ACCOUNT_HEADERS,
            )
        )

    def purchase_ship(self, ship_type: str, waypoint_symbol: str) -> ShipPurchase:
        return ShipPurchase.from_dict(
            data=self._post_endpoint_response(
                endpoint="/my/ships",
                headers=ACCOUNT_HEADERS,
                payload={
                    "shipType": ship_type,
                    "waypointSymbol": waypoint_symbol
                },
            )
        )

    def orbit_ship(self, ship_symbol: str) -> ShipPurchaseShipNav:
        return ShipPurchaseShipNav.from_dict(
            data=self._post_endpoint_response_nav(
                endpoint=f"/my/ships/{ship_symbol}/orbit",
                headers=AUTHORIZATION_HEADERS,
            )
        )

    def navigate_ship(self, ship_symbol: str, waypoint_symbol: str) -> ToAsteroidNavigate:
        response = requests.post(
            url=f"{BASE_URL}/my/ships/{ship_symbol}/navigate",
            headers=AUTHORIZATION_HEADERS,
            json={
                "waypointSymbol": waypoint_symbol
            },
        )
        if response.status_code == 200 or response.status_code == 201:
            return ToAsteroidNavigate.from_dict(response.json())
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code} {response.json()}")

    def dock_ship(self, ship_symbol: str) -> ShipPurchaseShipNav:
        return ShipPurchaseShipNav.from_dict(
            data=self._post_endpoint_response_nav(
                endpoint=f"/my/ships/{ship_symbol}/dock",
                headers=AUTHORIZATION_HEADERS,
            )
        )

    def refuel_ship(self, ship_symbol: str) -> ShipRefuel:
        return ShipRefuel.from_dict(
            data=self._post_endpoint_response(
                endpoint=f"/my/ships/{ship_symbol}/refuel",
                headers=AUTHORIZATION_HEADERS,
            )
        )

    @classmethod
    def _get_endpoint_response(cls, endpoint: str, headers: dict):
        response = requests.get(f"{BASE_URL}{endpoint}",
                                headers=headers)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code} {response.json()}")

    @classmethod
    def _post_endpoint_response(cls, endpoint: str, headers: dict, payload: dict = None):
        response = requests.post(
            url=f"{BASE_URL}{endpoint}",
            headers=headers,
            json=payload,
        )
        if response.status_code == 200 or response.status_code == 201:
            return response.json()["data"]
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code} {response.json()}")

    @classmethod
    def _post_endpoint_response_nav(cls, endpoint: str, headers: dict, payload: dict = None):
        response = requests.post(
            url=f"{BASE_URL}{endpoint}",
            headers=headers,
            json=payload,
        )
        if response.status_code == 200 or response.status_code == 201:
            return response.json()["data"]["nav"]
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code} {response.json()}")


if __name__ == "__main__":
    from pprint import pprint
    from domain.entities.ships_available import ShipsAvailable

    space = SpaceTradersService()
    ships = space.get_ships()
    contracts = space.get_contracts()
    if not contracts:
        raise ValueError("No hay contratos")
    # account = space.get_account()
    # asteroids=space.find_engineered_asteroids(contracts[0].terms.deliver[0].system_symbol)
    #shipyards_infos = space.find_shipyards(system_symbol=contracts[0].terms.deliver[0].system_symbol)
    # available_ships_info = space.view_ship_available(system_symbol=contracts[0].terms.deliver[0].system_symbol,
    #                        waypoint_symbol=shipyards_infos[2].symbol)
    # orbiter=space.orbit_ship("GREEN-2")
    # docker = space.dock_ship("GREEN-2")
    # pprint(orbiter)
    # ship_purchaser=space.purchase_ship(ship_type="SHIP_MINING_DRONE",waypoint_symbol=available_ships_info.symbol)
    # refuel_ship = space.refuel_ship("GREEN-2")
    navigate = space.navigate_ship("GREEN-2", "X1-TC65-C42")
    pprint(navigate)
