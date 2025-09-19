from dataclasses import dataclass
from domain.entities.to_asteroid_navigate_fuel_consumed import ToAsteroidNavigateFuelConsumed

@dataclass
class ToAsteroidNavigateFuel:
    capacity: int
    consumed: ToAsteroidNavigateFuelConsumed
    current: int