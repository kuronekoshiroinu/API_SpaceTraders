from dataclasses import dataclass


@dataclass
class ExtractOreCargoInventory:
    description: str
    name: str
    symbol: str
    units: int

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            description= data["description"],
            name= data["name"],
            symbol= data["symbol"],
            units= data["units"],
        )

    @classmethod
    def from_list(cls, list_data:list[dict]) -> list["ExtractOreCargoInventory"]:
        inventories=[]
        for dict_data in list_data:
            inventories.append(
                cls.from_dict(dict_data)
            )
        return inventories

