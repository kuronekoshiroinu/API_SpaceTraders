from dataclasses import dataclass
from domain.entities.ship_purchase_ship_fuel_consumed import ShipPurchaseShipFuelConsumed

@dataclass
class ShipPurchaseShipFuel:
    capacity: int
    consumed: ShipPurchaseShipFuelConsumed
    current: int