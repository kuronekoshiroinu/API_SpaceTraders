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
            headers={ACCOUNT_HEADERS},
            json=payload
        )