from dataclasses import dataclass

@dataclass
class ShipyardChart:
    submitted_by: str
    submitted_on: str
    waypoint_symbol: str

    @classmethod
    def from_dict(cls, data: dict) :
        return cls(
            submitted_by=data["submittedBy"],
            submitted_on=data["submittedOn"],
            waypoint_symbol=data["waypointSymbol"]
        )
