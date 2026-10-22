from http import HTTPStatus
import requests
from requests import Response

from src.main.api.models.bank_deposit_request import BankDepositRequest
from src.main.api.models.bank_deposit_response import BankDepositResponse
from src.main.api.requests.requester import Requester


class BankDepositRequester(Requester):
    def post(self, bank_deposit_request: BankDepositRequest) -> BankDepositResponse | Response:
        url = f'{self.base_url}/account/deposit'
        response = requests.post(
            url=url,
            json=bank_deposit_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return BankDepositResponse(**response.json())
        return response