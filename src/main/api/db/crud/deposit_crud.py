from sqlalchemy.orm import Session
from src.main.api.db.models.account_table import Account



class DepositCrudDb:
    @staticmethod
    def get_balance_by_account_id(db: Session,account_id: int) -> Account | None:
        return db.query(Account).filter_by(id= account_id).first()