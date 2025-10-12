from dataclasses import dataclass

from src.traders.domain.entities.ship_purchase_ship_nav_route import ShipPurchaseShipNavRoute


@dataclass
class ShipPurchaseShipNav:
    flight_mode: str
    route: ShipPurchaseShipNavRoute
    status: str
    system_symbol: str
    waypoint_symbol: str

    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            flight_mode=data["flightMode"],
            route= ShipPurchaseShipNavRoute.from_dict(data["route"]),
            status=data["status"],
            system_symbol=data["systemSymbol"],
            waypoint_symbol=data["waypointSymbol"]
        )