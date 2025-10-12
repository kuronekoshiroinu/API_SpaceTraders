from dataclasses import dataclass
import json
from src.traders.domain.entities.ship_purchase import ShipPurchase

@dataclass
class ShipPurchasePresenter:
    ship_purchase: ShipPurchase

    @property
    def to_str(self) -> str:
        return json.dumps(self.ship_purchase.to_dict,indent=3)