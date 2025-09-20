from dataclasses import dataclass

@dataclass
class ShipInfoCrew:
    capacity: int
    required: int

    @classmethod
    def from_dict(cls, crew_data: dict) :
        return cls(
            capacity=crew_data["capacity"],
            required=crew_data["required"]
        )
