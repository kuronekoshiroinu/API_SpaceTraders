from dataclasses import dataclass
from aplication.use_cases.contract_getter import ContractGetter
from aplication.use_cases.shipyard_finder import ShipyardFinder
from domain.entities.ship_available_info_types import ShipAvailableInfoTypes
from domain.entities.ship_info import ShipInfo
from domain.entities.ship_info_crew import ShipInfoCrew
from domain.entities.ship_info_engine import ShipInfoEngine
from domain.entities.ship_info_frame import ShipInfoFrame
from domain.entities.ship_info_modules import ShipInfoModules
from domain.entities.ship_info_mounts import ShipInfoMounts
from domain.entities.ship_info_reactor import ShipInfoReactor
from domain.entities.ship_info_requirements import ShipInfoRequirements
from domain.entities.ships_available import ShipsAvailable
from domain.interfaces import UseCase
from domain.constants import BASE_URL, ACCOUNT_HEADERS
import requests


@dataclass
class ShipAvailableViewer(UseCase):
    system_symbol: str
    waypoint_symbol: str

    def execute(self, *args, **kwargs):
        url = f"{BASE_URL}/systems/{self.system_symbol}/waypoints/{self.waypoint_symbol}/shipyard"
        response = requests.get(url, headers=ACCOUNT_HEADERS)
        if response.status_code == 200:
            return self._parse_ships_availables_data(response.json())
        else:
            error_msg = response.json().get('error', {}).get('message', 'Error desconocido')
            raise ValueError(f"Error al obtener ships availables: {error_msg}")

    def _parse_ships_availables_data(self, ships_data: dict) -> ShipsAvailable:
        data = ships_data["data"]
        return ShipsAvailable(
            modifications_fee=data["modificationsFee"],
            ships_types=self._get_ships_available_types(data["shipTypes"]),
            ships=self._get_ships_available_data(data["ships"]),
            symbol=data["symbol"],
            transactions=data["transactions"],
        )

    @classmethod
    def _get_ships_available_types(cls, ships_available: list[dict]) -> list[ShipAvailableInfoTypes]:
        availables = []
        for ship_available in ships_available:
            availables.append(
                ShipAvailableInfoTypes(
                    type=ship_available["type"]
                )
            )
        return availables

    @classmethod
    def _get_ships_available_data(cls, ships: list[ShipInfo]) -> list[ShipInfo]:
        available = []
        for ship in ships:
            available.append(
                ShipInfo(
                    activity=ship["activity"],
                    crew=cls._get_ship_crew_data(ship["crew"]),
                    description=ship["description"],
                    engine=cls._get_ship_engine_data(ship["engine"]),
                    frame=cls._get_ship_frame_data(ship["frame"]),
                    modules=cls._get_ship_module_data(ship["modules"]),
                    mounts=cls._get_ship_mounts_data(ship["mounts"]),
                    name=ship["name"],
                    purchase_price=ship["purchasePrice"],
                    reactor=cls._get_ship_reactor_data(ship["reactor"]),
                    supply=ship["supply"],
                    type=ship["type"]
                )
            )
        return available

    @classmethod
    def _get_ship_crew_data(cls, crew_data: dict) -> ShipInfoCrew:
        return ShipInfoCrew(
            capacity=crew_data["capacity"],
            required=crew_data["required"]
        )

    @classmethod
    def _get_ship_engine_data(cls, engine_data: dict) -> ShipInfoEngine:
        return ShipInfoEngine(
            condition=engine_data["condition"],
            description=engine_data["description"],
            integrity=engine_data["integrity"],
            name=engine_data["name"],
            quality=engine_data["quality"],
            requirements=cls._get_ship_requirement_data(engine_data["requirements"]),
            speed=engine_data["speed"],
            symbol=engine_data["symbol"]
        )

    @classmethod
    def _get_ship_requirement_data(cls, requirement_data: dict) -> ShipInfoRequirements:
        return ShipInfoRequirements(
            crew=requirement_data.get("crew",None),
            power=requirement_data.get("power",None),
            slots=requirement_data.get("slots",None)
        )

    @classmethod
    def _get_ship_frame_data(cls, frame_data: dict) -> ShipInfoFrame:
        return ShipInfoFrame(
            condition=frame_data["condition"],
            description=frame_data["description"],
            fuel_capacity=frame_data["fuelCapacity"],
            integrity=frame_data["integrity"],
            module_slots=frame_data["moduleSlots"],
            mounting_points=frame_data["mountingPoints"],
            name=frame_data["name"],
            quality=frame_data["quality"],
            requirements=cls._get_ship_requirement_data(frame_data["requirements"]),
            symbol=frame_data["symbol"]
        )
    @classmethod
    def _get_ship_module_data(cls, modules_data: list[dict]) -> list[ShipInfoModules]:
        ships_info_modules=[]

        for module in modules_data:
            ships_info_modules.append(
                ShipInfoModules(
                    description=module["description"],
                    name=module["name"],
                    requirements=cls._get_ship_requirement_data(module["requirements"]),
                    symbol=module["symbol"],
                    capacity=module.get("capacity"),
                )
            )
        return ships_info_modules

    @classmethod
    def _get_ship_mounts_data(cls, mounts_data:list[dict])-> list[ShipInfoMounts]:
        mounts=[]
        for mount in mounts_data:
            mounts.append(
                ShipInfoMounts(
                    description=mount["description"],
                    name=mount["name"],
                    requirements=cls._get_ship_requirement_data(mount["requirements"]),
                    strength=mount["strength"],
                    symbol=mount["symbol"],
                    deposits=list(mount["deposits"]) if mount.get("deposits",None) else None,
                )
            )
        return mounts
    @classmethod
    def _get_ship_reactor_data(cls, reactor_data:dict) -> ShipInfoReactor:
        return ShipInfoReactor(
            condition= reactor_data["condition"],
            description=reactor_data["description"],
            integrity=reactor_data["integrity"],
            name=reactor_data["name"],
            power_output= reactor_data["powerOutput"],
            quality=reactor_data["quality"],
            requirements=cls._get_ship_requirement_data(reactor_data["requirements"]),
            symbol=reactor_data["symbol"],
        )




if __name__ == '__main__':
    from pprint import pprint

    contracts = ContractGetter().execute()
    shipyard_info = ShipyardFinder(contracts[0].terms.deliver[0].system_symbol).execute()
    pprint(shipyard_info)
    #print(shipyard_info[1].symbol)

    ship_availables = ShipAvailableViewer(contracts[0].terms.deliver[0].system_symbol, shipyard_info[2].symbol).execute()
    pprint(ship_availables)
