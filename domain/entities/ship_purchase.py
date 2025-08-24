from dataclasses import dataclass
from domain.entities.ship_purchase_agent import ShipPurchaseAgent
from domain.entities.ship_purchase_ship import ShipPurchaseShip
from domain.entities.ship_purchase_transaction import ShipPurchaseTransaction


@dataclass
class ShipPurchase:
    agent: ShipPurchaseAgent
    ship: ShipPurchaseShip
    transaction: ShipPurchaseTransaction