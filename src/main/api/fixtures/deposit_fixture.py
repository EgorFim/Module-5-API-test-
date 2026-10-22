import pytest
from src.main.api.models.bank_deposit_request import BankDepositRequest


@pytest.fixture
def deposit_body(api_manager, create_user_request):
    response =  api_manager.user_steps.create_account(create_user_request)
    user_request = BankDepositRequest(accountId=response.id, amount=1000.5)
    return user_request


@pytest.fixture
def deposit_body_invalid(api_manager, create_user_request):
    response =  api_manager.user_steps.create_account(create_user_request)
    user_request = BankDepositRequest(accountId=response.id, amount=999.9)
    return user_request