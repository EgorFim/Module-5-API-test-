from src.main.api.db.models.credit_table import Credit
from sqlalchemy.orm import Session



class CreditCrudDb:
    @staticmethod
    def get_balance_from_id(db: Session,credit_id:int) -> Credit | None:
        return db.query(Credit).filter_by(account_id=credit_id).first()