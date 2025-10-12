from dataclasses import dataclass

from src.traders.domain.entities.ship_info_engine import ShipInfoEngine


@dataclass
class ShipPurchaseShipPresenter:
    engine: ShipInfoEngine
    modules: list
