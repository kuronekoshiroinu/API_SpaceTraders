from fastapi import FastAPI

from src.traders.aplication.use_cases.simple_contract_getter import SimpleContractGetter
from src.traders.infraestructure.services.space_traders_service import SpaceTradersService

app = FastAPI(title="contract", version="1.0.0")


@app.get("/contrato")
def get_contract_type():
    return SimpleContractGetter(
        trader_service=SpaceTradersService(),
    ).execute()
