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
            return ShipPurchase.from_dict(response.json()["data"])
        else:
            error_msg = response.json().get('error', {}).get('message', 'Error desconocido')
            raise ValueError(f"Error al obtener ship purchase: {error_msg} statusCode: {response.status_code}")


if __name__ == '__main__':
    from pprint import pprint
    ship_purch=ShipPurchaser(
        ship_type="SHIP_MINING_DRONE",
        waypoint_symbol="X1-ZK44-H49"
    )
    ship_data=ship_purch.execute()
    pprint(ship_data)

