from dataclasses import dataclass
from domain.entities.to_asteroid_navigate_fuel_consumed import ToAsteroidNavigateFuelConsumed

@dataclass
class ToAsteroidNavigateFuel:
    capacity: int
    consumed: ToAsteroidNavigateFuelConsumed
    current: int

    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            capacity=data["capacity"],
            consumed=ToAsteroidNavigateFuelConsumed.from_dict(data["consumed"]),
            current=data["current"]
        )