from dataclasses import dataclass

from domain.entities.ship_info_engine import ShipInfoEngine
from domain.entities.ship_info_frame import ShipInfoFrame
from domain.entities.ship_info_mounts import ShipInfoMounts
from domain.entities.ship_info_reactor import ShipInfoReactor
from domain.entities.ship_purchase_ship_cargo import ShipPurchaseShipCargo
from domain.entities.ship_purchase_ship_cooldown import ShipPurchaseShipCooldown
from domain.entities.ship_purchase_ship_crew import ShipPurchaseShipCrew
from domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from domain.entities.ship_purchase_ship_registration import ShipPurchaseShipRegistration
from domain.entities.to_asteroid_navigate_fuel import ToAsteroidNavigateFuel


@dataclass
class ShipPurchaseShip:
    cargo: ShipPurchaseShipCargo
    cooldown: ShipPurchaseShipCooldown
    crew: ShipPurchaseShipCrew
    engine: ShipInfoEngine
    frame: ShipInfoFrame
    fuel: ToAsteroidNavigateFuel
    modules: list
    mounts: list[ShipInfoMounts]
    nav: ShipPurchaseShipNav
    reactor: ShipInfoReactor
    registration: ShipPurchaseShipRegistration
    symbol: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            cargo=ShipPurchaseShipCargo.from_dict(data["cargo"]),
            cooldown=ShipPurchaseShipCooldown.from_dict(data["cooldown"]),
            crew=ShipPurchaseShipCrew.from_dict(data["crew"]),
            engine=ShipInfoEngine.from_dict(data["engine"]),
            frame=ShipInfoFrame.from_dict(data["frame"]),
            fuel=ToAsteroidNavigateFuel.from_dict(data["fuel"]),
            modules=[],  # TODO CREAR ENTIDAD O BUSCAR
            mounts=cls._get_ship_mounts_data(data["mounts"]),
            nav=ShipPurchaseShipNav.from_dict(data["nav"]),
            reactor=ShipInfoReactor.from_dict(data["reactor"]),
            registration=ShipPurchaseShipRegistration.from_dict(data["registration"]),
            symbol=data["symbol"],
        )

    @classmethod
    def _get_ship_mounts_data(cls, mounts_data: list[dict]) -> list[ShipInfoMounts]:
        mounts = []
        for mount in mounts_data:
            mounts.append(
                ShipInfoMounts.from_dict(mount)
            )
        return mounts
