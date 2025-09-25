from domain.entities.ship_purchase import ShipPurchase
from domain.interfaces import UseCase
from domain.constants import BASE_URL, ACCOUNT_HEADERS
from dataclasses import dataclass
import requests
@dataclass
class ShipPurchaser(UseCase):
    ship_type: str
    waypoint_symbol: str

    def execute(self,*args,**kwargs):
        url = f"{BASE_URL}/my/ships"
        payload = {
            "shipType": self.ship_type,
            "waypointSymbol": self.waypoint_symbol
        }

        response = requests.post(
            url,
            headers=ACCOUNT_HEADERS,
            json=payload
        )
        print(response.status_code)
        #return response.json()
        if response.status_code in (200, 201):
            return self._parse_ship_purchase_data(response.json())
        else:
            error_msg = response.json().get('error', {}).get('message', 'Error desconocido')
            raise ValueError(f"Error al obtener ship purchase: {error_msg} statusCode: {response.status_code}")

    def _parse_ship_purchase_data(self, shipp_data: dict) -> ShipPurchase:
        data=shipp_data["data"]
        return ShipPurchase(
            agent=data["agent"],
            ship=data["ship"],
            transaction=data["transaction"]
        )

if __name__ == '__main__':
    from pprint import pprint
    ship_purch=ShipPurchaser(
        ship_type="SHIP_MINING_DRONE",
        waypoint_symbol="X1-CY20-H53"
    )
    ship_data=ship_purch.execute()
    pprint(ship_data)

