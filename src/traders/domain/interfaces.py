from abc import ABC, abstractmethod

from src.traders.domain.entities.account import Account
from src.traders.domain.entities.contract import Contract
from src.traders.domain.entities.engineered_asteroid import EngineeredAsteroid
from src.traders.domain.entities.ship_purchase_ship import ShipPurchaseShip


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
