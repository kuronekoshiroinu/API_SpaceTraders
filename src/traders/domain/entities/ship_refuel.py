from dataclasses import dataclass

from src.traders.domain.entities.ship_purchase_agent import ShipPurchaseAgent
from src.traders.domain.entities.ship_refuel_transaction import ShipRefuelTransaction
from src.traders.domain.entities.to_asteroid_navigate_fuel import ToAsteroidNavigateFuel


@dataclass
class ShipRefuel:
    agent: ShipPurchaseAgent
    fuel: ToAsteroidNavigateFuel
    transaction:ShipRefuelTransaction

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            agent=ShipPurchaseAgent.from_dict(data["agent"]),
            fuel=ToAsteroidNavigateFuel.from_dict(data["fuel"]),
            transaction=ShipRefuelTransaction.from_dict(data["transaction"])
        )