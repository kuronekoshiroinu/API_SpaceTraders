from dataclasses import dataclass

import requests

from domain.constants import BASE_URL, AUTHORIZATION_HEADERS
from domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from domain.entities.to_asteroid_navigate import ToAsteroidNavigate
from domain.entities.to_asteroid_navigate_fuel import ToAsteroidNavigateFuel
from domain.entities.to_asteroid_navigate_fuel_consumed import ToAsteroidNavigateFuelConsumed


@dataclass
class ShipNavigater:
    mining_ship_symbol: str
    waypoint_symbol:str
    def execute(self, *args, **kwargs):
        url = f"{BASE_URL}/my/ships/{self.mining_ship_symbol}/navigate"
        headers = {
            **AUTHORIZATION_HEADERS,
            "Content-Type": "application/json"
        }
        payload = {
            "waypointSymbol": self.waypoint_symbol
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=15
            )

            if response.status_code not in (200, 201):
                error_data = response.json()
                error_msg = error_data.get('error', {}).get('message', 'Error desconocido')
                raise ValueError(f"Error al navegar: {error_msg}")

            #return response.json()
            return self._parse_asteroid_navigator(response.json())

        except requests.exceptions.JSONDecodeError:
            raise ValueError("Respuesta no es JSON válido")
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error de red: {str(e)}")

    def _parse_asteroid_navigator(self, asteroid_data: dict) -> ToAsteroidNavigate:
        data=asteroid_data["data"]
        return ToAsteroidNavigate(
            events=data["events"],
            fuel=self._get_navigate_fuel(data["fuel"]),
            nav=ShipPurchaseShipNav.from_dict(data["nav"])
        )
    @classmethod
    def _get_navigate_fuel(cls, navigate_fuel:dict) ->ToAsteroidNavigateFuel:
        return ToAsteroidNavigateFuel(
            capacity=navigate_fuel["capacity"],
            consumed=cls._get_navigate_fuel_consumed(navigate_fuel["consumed"]),
            current=navigate_fuel["current"]
        )
    @classmethod
    def _get_navigate_fuel_consumed(cls, fuel_consumed: dict)-> ToAsteroidNavigateFuelConsumed:
        return ToAsteroidNavigateFuelConsumed(
            amount=fuel_consumed["amount"],
            timestamp=fuel_consumed["timestamp"]
        )

if __name__=="__main__":
    from pprint import pprint
    flyer=ShipNavigater("AGENT_BLUE-4", "X1-RH66-A2").execute()
    pprint(flyer)
