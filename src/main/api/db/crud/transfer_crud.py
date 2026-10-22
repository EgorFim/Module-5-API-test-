from sqlalchemy.orm import Session
from src.main.api.db.models.transaction_table import Transaction
from src.main.api.db.models.account_table import Account


class TransactionCrudDb:
    @staticmethod
    def get_transfer_by_from_account_id(db: Session, from_id: int) -> Transaction | None:
        return db.query(Transaction).filter_by(from_account_id=from_id).first()

    @staticmethod
    def get_transfer_by_from_account_id_not(db: Session, account_id: int) -> Account | None:
        return db.query(Account).filter_by(id=account_id).first()

