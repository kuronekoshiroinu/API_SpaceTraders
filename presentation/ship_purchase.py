from dataclasses import dataclass

from domain.entities.ship_purchase_ship import ShipPurchaseShip
from presentation.ship_purchase_ship import ShipPurchaseShipPresenter


@dataclass
class ShipPurchasePresenter:
    ship: ShipPurchaseShipPresenter
