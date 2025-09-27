from dataclasses import dataclass
from src.traders.domain.entities.ship_purchase_agent import ShipPurchaseAgent
from src.traders.domain.entities.ship_purchase_ship import ShipPurchaseShip
from src.traders.domain.entities.ship_purchase_transaction import ShipPurchaseTransaction


@dataclass
class ShipPurchase:
    agent: ShipPurchaseAgent
    ship: ShipPurchaseShip
    transaction: ShipPurchaseTransaction

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            agent=ShipPurchaseAgent.from_dict(data["agent"]),
            ship=ShipPurchaseShip.from_dict(data["ship"]),
            transaction=ShipPurchaseTransaction.from_dict(data["transaction"]),
        )