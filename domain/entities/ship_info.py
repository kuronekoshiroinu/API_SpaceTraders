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
