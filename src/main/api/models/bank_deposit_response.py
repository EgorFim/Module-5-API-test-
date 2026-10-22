from src.main.api.models.base_model import BaseModel


class BankDepositResponse(BaseModel):
    id: int
    balance: float