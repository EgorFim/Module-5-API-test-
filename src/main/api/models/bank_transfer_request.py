from src.main.api.models.base_model import BaseModel



class BankTransferRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: float