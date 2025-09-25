from dataclasses import dataclass

import requests

from domain.constants import BASE_URL, AUTHORIZATION_HEADERS
from domain.entities.to_asteroid_navigate import ToAsteroidNavigate


@dataclass
class ShipNavigater:
    mining_ship_symbol: str
    waypoint_symbol: str

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

            # return response.json()
            return ToAsteroidNavigate.from_dict(response.json())

        except requests.exceptions.JSONDecodeError:
            raise ValueError("Respuesta no es JSON válido")
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error de red: {str(e)}")


if __name__ == "__main__":
    from pprint import pprint

    flyer = ShipNavigater("AGENT_BLUE-4", "X1-CY20-XZ5Z").execute()
    pprint(flyer)
