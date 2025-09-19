from dataclasses import dataclass

from domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from domain.entities.to_asteroid_navigate_fuel import ToAsteroidNavigateFuel

@dataclass
class ToAsteroidNavigate:
    events: list
    fuel:ToAsteroidNavigateFuel
    nav: ShipPurchaseShipNav

