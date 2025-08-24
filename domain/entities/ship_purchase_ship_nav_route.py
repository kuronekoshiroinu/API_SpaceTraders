from dataclasses import dataclass

from domain.entities.ship_purchase_ship_ubication import ShipPurchaseShipUbication


@dataclass
class ShipPurchaseShipNavRoute:
    arrival: str
    departure_time: str
    destination: ShipPurchaseShipUbication
    origin: ShipPurchaseShipUbication
