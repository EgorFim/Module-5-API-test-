from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_secret_request import CreateUserSecretRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self,create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username,password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def create_account_secret(self,create_user_secret_request: CreateUserSecretRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_secret_request.username,password=create_user_secret_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response


    def make_deposit(self,create_user_request: CreateUserRequest,deposit_body):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,password=create_user_request.password),
            Endpoint.MAKE_DEPOSIT,
            ResponseSpecs.request_ok()
        ).post(deposit_body)
        return response



    def make_deposit_invalid(self,create_user_request: CreateUserRequest,deposit_body_invalid):
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,password=create_user_request.password),
            Endpoint.MAKE_DEPOSIT,
            ResponseSpecs.request_bad()
        ).post(deposit_body_invalid)


    def make_transfer(self,create_user_request: CreateUserRequest,transfer_body):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,password=create_user_request.password),
            Endpoint.MAKE_TRANSFER,
            ResponseSpecs.request_ok()
        ).post(transfer_body)
        return response

    def make_transfer_invalid(self,create_user_request: CreateUserRequest,transfer_body_invalid):
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,password=create_user_request.password),
            Endpoint.MAKE_TRANSFER,
            ResponseSpecs.request_bad()
        ).post(transfer_body_invalid)


    def take_credit(self, create_user_secret_request: CreateUserSecretRequest,credit_body):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_secret_request.username,password=create_user_secret_request.password
            ),
            Endpoint.TAKE_CREDIT,
            ResponseSpecs.request_created()
        ).post(credit_body)
        return response


    def take_credit_invalid(self, create_user_request: CreateUserRequest,credit_body_inv):
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,password=create_user_request.password
            ),
            Endpoint.TAKE_CREDIT,
            ResponseSpecs.request_forbidden()
        ).post(credit_body_inv)


    def credit_repay(self, create_user_secret_request: CreateUserSecretRequest,credit_repay_body):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_secret_request.username,password=create_user_secret_request.password
            ),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.request_ok()
        ).post(credit_repay_body)
        return response

    def credit_repay_inv(self, create_user_secret_request: CreateUserSecretRequest,credit_repay_body_inv):
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_secret_request.username,password=create_user_secret_request.password
            ),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.request_unprocessable()
        ).post(credit_repay_body_inv)

