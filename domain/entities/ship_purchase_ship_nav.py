from dataclasses import dataclass

from domain.entities.ship_purchase_ship_nav_route import ShipPurchaseShipNavRoute


@dataclass
class ShipPurchaseShipNav:
    flight_mode: str
    route: ShipPurchaseShipNavRoute
    status: str
    system_symbol: str
    waypoint_symbol: str