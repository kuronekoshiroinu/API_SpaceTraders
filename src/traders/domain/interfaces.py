from abc import ABC, abstractmethod

from src.traders.domain.entities.account import Account
from src.traders.domain.entities.contract import Contract
from src.traders.domain.entities.engineered_asteroid import EngineeredAsteroid
from src.traders.domain.entities.ship_purchase import ShipPurchase
from src.traders.domain.entities.ship_purchase_ship import ShipPurchaseShip
from src.traders.domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from src.traders.domain.entities.ships_available import ShipsAvailable
from src.traders.domain.entities.shipyard import Shipyard


class UseCase(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError


class TradersService(ABC):
    @abstractmethod
    def get_account(self) -> Account:
        raise NotImplementedError

    @abstractmethod
    def get_contracts(self) -> list[Contract]:
        raise NotImplementedError

    @abstractmethod
    def get_ships(self) -> list[ShipPurchaseShip]:
        raise NotImplementedError

    @abstractmethod
    def find_engineered_asteroids(self, system_symbol: str) -> list[EngineeredAsteroid]:
        raise NotImplementedError

    @abstractmethod
    def orbit_ship(self, ship_symbol: str) -> ShipPurchaseShipNav:
        raise NotImplementedError

    @abstractmethod
    def purchase_ship(self, ship_type: str, waypoint_symbol: str) -> ShipPurchase:
        raise NotImplementedError
    @abstractmethod
    def find_shipyards(self, system_symbol: str) -> list[Shipyard]:
        raise NotImplementedError
    @abstractmethod
    def view_ship_available(self, system_symbol: str, waypoint_symbol: str) -> ShipsAvailable:
        raise NotImplementedError
