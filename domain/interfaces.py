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
    def get_account(self) -> Account:
        raise NotImplementedError

    @abstractmethod
    def get_contract(self) -> list[Contract]:
        raise NotImplementedError

    @abstractmethod
    def get_ships(self)->list[ShipPurchaseShip]:
        raise NotImplementedError
