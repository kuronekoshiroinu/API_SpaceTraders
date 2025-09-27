from dataclasses import dataclass

from src.traders.domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from src.traders.domain.entities.to_asteroid_navigate_fuel import ToAsteroidNavigateFuel


@dataclass
class ToAsteroidNavigate:
    events: list
    fuel:ToAsteroidNavigateFuel
    nav: ShipPurchaseShipNav

    @classmethod
    def from_dict(cls, data: dict):
        data=data["data"]
        return cls(
            events=data["events"],
            fuel=ToAsteroidNavigateFuel.from_dict(data["fuel"]),
            nav=ShipPurchaseShipNav.from_dict(data["nav"])
        )

