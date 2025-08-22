from dataclasses import dataclass
from domain.entities.ship_info_engine import ShipInfoEngine
from domain.entities.ship_info_frame import ShipInfoFrame
from domain.entities.ship_info_mounts import ShipInfoMounts
from domain.entities.ship_info_reactor import ShipInfoReactor
from domain.entities.ship_purchase_ship_cargo import ShipPurchaseShipCargo
from domain.entities.ship_purchase_ship_cooldown import ShipPurchaseShipCooldown
from domain.entities.ship_purchase_ship_crew import ShipPurchaseShipCrew
from domain.entities.ship_purchase_ship_fuel import ShipPurchaseShipFuel
from domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from domain.entities.ship_purchase_ship_registration import ShipPurchaseShipRegistration

@dataclass
class ShipPurchaseShip:
    cargo:ShipPurchaseShipCargo
    cooldown: ShipPurchaseShipCooldown
    crew: ShipPurchaseShipCrew
    engine: ShipInfoEngine
    frame: ShipInfoFrame
    fuel: ShipPurchaseShipFuel
    modules: list
    mounts: ShipInfoMounts
    nav: ShipPurchaseShipNav
    reactor: ShipInfoReactor
    registrations: ShipPurchaseShipRegistration
    symbol: str