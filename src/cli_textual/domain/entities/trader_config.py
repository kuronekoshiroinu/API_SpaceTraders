import json
from dataclasses import dataclass, asdict


@dataclass
class TraderConfig:
    contract_system_symbol: str
    shipyard_waypoint_symbol: str
    shipyard_available_system_symbol: str

    @property
    def to_dict(self)->dict:
        return asdict(self)

    @property
    def to_str(self) -> str:
        return json.dumps(self.to_dict, indent=3)
