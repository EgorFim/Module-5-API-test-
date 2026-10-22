import pytest
from src.main.api.models.bank_deposit_request import BankDepositRequest
from src.main.api.models.bank_transfer_request import BankTransferRequest


@pytest.fixture
def transfer_body(api_manager, create_user_request):
    acc_1 =  api_manager.user_steps.create_account(create_user_request)
    acc_2 = api_manager.user_steps.create_account(create_user_request)
    user_request = BankDepositRequest(accountId=acc_1.id, amount=2000)
    api_manager.user_steps.make_deposit(create_user_request,user_request)
    user_request = BankTransferRequest(
            fromAccountId=acc_1.id, toAccountId=acc_2.id, amount=500)
    return user_request


@pytest.fixture
def transfer_body_invalid(api_manager, create_user_request):
    acc_1 =  api_manager.user_steps.create_account(create_user_request)
    acc_2 = api_manager.user_steps.create_account(create_user_request)
    user_request = BankDepositRequest(accountId=acc_1.id, amount=2000)
    api_manager.user_steps.make_deposit(create_user_request,user_request)
    user_request = BankTransferRequest(
            fromAccountId=acc_1.id, toAccountId=acc_2.id, amount=499.9)
    return user_request