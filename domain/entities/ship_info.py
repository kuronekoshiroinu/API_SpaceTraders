from dataclasses import dataclass
from domain.entities.ship_info_crew import ShipInfoCrew
from domain.entities.ship_info_engine import ShipInfoEngine
from domain.entities.ship_info_frame import ShipInfoFrame
from domain.entities.ship_info_modules import ShipInfoModules
from domain.entities.ship_info_mounts import ShipInfoMounts
from domain.entities.ship_info_reactor import ShipInfoReactor


@dataclass
class ShipInfo:
    activity: str
    crew: ShipInfoCrew
    description: str = None
    engine: ShipInfoEngine = None
    frame: ShipInfoFrame = None
    modules: list[ShipInfoModules] = None
    mounts: list[ShipInfoMounts] = None
    name: str = None
    purchase_price: int = None
    reactor: ShipInfoReactor = None
    supply: str = None
    type: str = None

    @classmethod
    def from_list(cls, ships: list[dict]) -> list["ShipInfo"]:
        available = []
        for ship in ships:
            available.append(
                cls(
                    activity=ship["activity"],
                    crew=ShipInfoCrew.from_dict(ship["crew"]),
                    description=ship["description"],
                    engine=ShipInfoEngine.from_dict(ship["engine"]),
                    frame=ShipInfoFrame.from_dict(ship["frame"]),
                    modules=ShipInfoModules.from_list(ship["modules"]),
                    mounts=ShipInfoMounts.from_list(ship["mounts"]),
                    name=ship["name"],
                    purchase_price=ship["purchasePrice"],
                    reactor=ShipInfoReactor.from_dict(ship["reactor"]),
                    supply=ship["supply"],
                    type=ship["type"]
                )
            )
        return available
