from dataclasses import dataclass

@dataclass
class ShipyardChart:
    submitted_by: str
    submitted_on: str
    waypoint_symbol: str