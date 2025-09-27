from dataclasses import dataclass

from src.traders.domain.entities.ship_purchase_ship_ubication import ShipPurchaseShipUbication


@dataclass
class ShipPurchaseShipNavRoute:
    arrival: str
    departure_time: str
    destination: ShipPurchaseShipUbication
    origin: ShipPurchaseShipUbication

    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            arrival=data["arrival"],
            departure_time=data["departureTime"],
            destination=ShipPurchaseShipUbication.from_dict(data["destination"]),
            origin=ShipPurchaseShipUbication.from_dict(data["origin"])
        )
