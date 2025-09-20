from abc import ABC, abstractmethod

from domain.entities.account import Account
from domain.entities.contract import Contract
from domain.entities.ship_purchase_ship import ShipPurchaseShip


class UseCase(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError


class TradersService(ABC):
    @abstractmethod
    def get_account(self, data: dict) -> Account:
        raise NotImplementedError

    @abstractmethod
    def get_contract(self, data: list[dict]) -> list[Contract]:
        raise NotImplementedError

    @abstractmethod
    def get_ships(self, data:list[dict])->list[ShipPurchaseShip]:
        raise NotImplementedError
