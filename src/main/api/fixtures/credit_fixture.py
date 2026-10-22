import pytest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request import CreditRequest


@pytest.fixture
def credit_body(api_manager, create_user_secret_request):
    response =  api_manager.user_steps.create_account(create_user_secret_request)
    user_request = CreditRequest(accountId=response.id,amount =5000,termMonths=12)
    return user_request


@pytest.fixture
def credit_body_inv(api_manager, create_user_request):
    response =  api_manager.user_steps.create_account(create_user_request)
    user_request = CreditRequest(accountId=response.id,amount =5000,termMonths=12)
    return user_request


@pytest.fixture
def credit_repay_body(api_manager, create_user_secret_request):
    response =  api_manager.user_steps.create_account(create_user_secret_request)
    user_request = CreditRequest(accountId=response.id,amount =5000,termMonths=12)
    cred = api_manager.user_steps.take_credit(create_user_secret_request, user_request)
    cred_id = cred.creditId
    acc_for_cred_id = cred.accountId
    cred_repay = CreditRepayRequest(creditId=cred_id, accountId=acc_for_cred_id, amount=5000)
    return cred_repay

@pytest.fixture
def repay_body_inv(api_manager, create_user_secret_request):
    response =  api_manager.user_steps.create_account(create_user_secret_request)
    user_request = CreditRequest(accountId=response.id,amount =5000,termMonths=12)
    cred = api_manager.user_steps.take_credit(create_user_secret_request, user_request)
    cred_id = cred.creditId
    acc_for_cred_id = cred.accountId
    cred_repay = CreditRepayRequest(creditId=cred_id, accountId=acc_for_cred_id, amount=4000)
    return cred_repay

