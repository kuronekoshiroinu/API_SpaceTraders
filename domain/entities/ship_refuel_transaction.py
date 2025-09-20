from dataclasses import dataclass

@dataclass
class ShipRefuelTransaction:
    price_per_unit:int
    ship_symbol:str
    timestamp:str
    total_price: int
    trade_symbol: str
    type:str
    units:int
    waypoint_symbol:str

    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            price_per_unit=data["pricePerUnit"],
            ship_symbol=data["shipSymbol"],
            timestamp=data["timestamp"],
            total_price=data["totalPrice"],
            trade_symbol=data["tradeSymbol"],
            type=data["type"],
            units=data["units"],
            waypoint_symbol=data["waypointSymbol"]
        )