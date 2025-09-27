from dataclasses import dataclass

from src.traders.presentation.ship_purchase_ship import ShipPurchaseShipPresenter


@dataclass
class ShipPurchasePresenter:
    ship: ShipPurchaseShipPresenter
