from dataclasses import dataclass
from domain.constants import BASE_URL, AUTHORIZATION_HEADERS
import requests

from domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from domain.entities.ship_purchase_ship_nav_route import ShipPurchaseShipNavRoute
from domain.entities.ship_purchase_ship_ubication import ShipPurchaseShipUbication


@dataclass
class ToAsteroidFlyer:
    mining_ship_symbol: str

    def execute(self, *args, **kwargs) :
        response = requests.post(f"{BASE_URL}/my/ships/{self.mining_ship_symbol}/orbit",
                              headers=AUTHORIZATION_HEADERS)
        if response.status_code == 200:
            return self._parse_ship_flyer(response.json()["data"]["nav"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")

    def _parse_ship_flyer(self, ship_data:dict) -> ShipPurchaseShipNav:
        return ShipPurchaseShipNav(
            flight_mode=ship_data["flightMode"],
            route=self._get_ship_flyer_route(ship_data["route"]),
            status=ship_data["status"],
            system_symbol=ship_data["systemSymbol"],
            waypoint_symbol=ship_data["waypointSymbol"]
        )

    @classmethod
    def _get_ship_flyer_route(cls, data:dict)->ShipPurchaseShipNavRoute:
        return ShipPurchaseShipNavRoute(
            arrival=data["arrival"],
            departure_time=data["departureTime"],
            destination=cls._get_ship_flyer_ubication(data["destination"]),
            origin=cls._get_ship_flyer_ubication(data["origin"])
        )

    @classmethod
    def _get_ship_flyer_ubication(cls, data:dict)->ShipPurchaseShipUbication:
        return ShipPurchaseShipUbication(
            symbol=data["symbol"],
            system_symbol=data["systemSymbol"],
            type=data["type"],
            x=data["x"],
            y=data["y"]
        )


if __name__=="__main__":
    from pprint import pprint
    flyer=ToAsteroidFlyer("AGENT_ROUGE-3").execute()
    pprint(flyer)
