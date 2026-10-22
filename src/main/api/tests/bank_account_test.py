import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from src.main.api.fixtures.db_fixture import db_session
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.db.crud.deposit_crud import DepositCrudDb as Deposit
from src.main.api.db.crud.transfer_crud import TransactionCrudDb as Transfer
from src.main.api.db.crud.account_crud import AccountCrudDb as Account



@pytest.mark.api
class TestBankAccount:
    def test_deposit_succesful(self,api_manager: ApiManager,create_user_request: CreateUserRequest,deposit_body,db_session: Session):

        response = api_manager.user_steps.make_deposit(create_user_request,deposit_body)
        assert response.balance == deposit_body.amount
        account_from_db = Deposit.get_balance_by_account_id(db_session, response.id)
        assert account_from_db.balance == deposit_body.amount, 'Баланс счета в БД не изменился'







    def test_deposit_unsuccesful(self,api_manager: ApiManager,create_user_request: CreateUserRequest,deposit_body_invalid,db_session: Session):
        api_manager.user_steps.make_deposit_invalid(create_user_request, deposit_body_invalid)
        deposit_from_db = Deposit.get_balance_by_account_id(db_session, deposit_body_invalid.accountId)
        assert deposit_from_db.balance == 0, "Баланс счета в БД изменился"






    def test_transfer_valid(self,api_manager: ApiManager,create_user_request: CreateUserRequest,transfer_body,db_session: Session):
        response = api_manager.user_steps.make_transfer(create_user_request, transfer_body)
        assert response.fromAccountIdBalance == 1500
        transfer_from_db = Transfer.get_transfer_by_from_account_id(db_session, transfer_body.fromAccountId)
        assert transfer_from_db.from_account_id == response.fromAccountId, "Аккаунт не найден в БД"




    def test_transfer_invalid(self,api_manager: ApiManager,create_user_request: CreateUserRequest,transfer_body_invalid,db_session: Session):
        balance_before = Account.get_account_by_id(db_session, transfer_body_invalid.fromAccountId)
        api_manager.user_steps.make_transfer_invalid(create_user_request, transfer_body_invalid)
        invalid_transfer_bd = Transfer.get_transfer_by_from_account_id_not(db_session, transfer_body_invalid.fromAccountId)
        assert invalid_transfer_bd.balance == balance_before.balance, "Баланс после операции отличается в БД"



    def test_credit_valid(self,api_manager: ApiManager,create_user_secret_request: CreateUserRequest,credit_body,db_session: Session):
        response = api_manager.user_steps.take_credit(create_user_secret_request, credit_body)
        assert response.balance == credit_body.amount
        credit_from_db = Credit.get_balance_from_id(db_session, response.accountId)
        assert credit_from_db.amount == response.amount, 'Сумма запроса в БД отличается от фактической'



    def test_credit_invalid(self,api_manager: ApiManager,create_user_request: CreateUserRequest,credit_body_inv,db_session: Session):
        balance_before = Account.get_account_by_id(db_session, credit_body_inv.accountId)
        api_manager.user_steps.take_credit_invalid(create_user_request, credit_body_inv)
        credit_from_db = Account.get_account_by_id(db_session, credit_body_inv.accountId)
        assert credit_from_db.balance == balance_before.balance, 'Данные о кредите появились в БД'


    def test_repay_credit_done(self,api_manager: ApiManager,create_user_secret_request: CreateUserRequest,credit_repay_body,db_session):
        credit_before_repay_db = Credit.get_balance_from_id(db_session, credit_repay_body.accountId)
        response = api_manager.user_steps.credit_repay(create_user_secret_request, credit_repay_body)
        assert response.amountDeposited == credit_repay_body.amount
        credit_after_repay_from_db = Credit.get_balance_from_id(db_session, credit_repay_body.accountId)
        assert credit_after_repay_from_db.balance == credit_before_repay_db.balance, 'Баланс не изменился в БД после погашения'



    def test_repay_credit_not_done(self,api_manager: ApiManager,create_user_secret_request: CreateUserRequest,repay_body_inv,db_session):
        credit_before_repay_db = Credit.get_balance_from_id(db_session, repay_body_inv.accountId)
        api_manager.user_steps.credit_repay_inv(create_user_secret_request, repay_body_inv)
        credit_after_repay_from_db = Credit.get_balance_from_id(db_session, repay_body_inv.accountId)
        assert credit_after_repay_from_db.balance == credit_before_repay_db.balance, 'Баланс изменился в БД'









