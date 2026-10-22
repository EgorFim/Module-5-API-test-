import requests
from requests import Response
from src.main.api.models.bank_transfer_request import BankTransferRequest
from src.main.api.models.bank_transfer_response import BankTransferResponse
from src.main.api.requests.requester import Requester
from http import HTTPStatus


class BankTransferRequester(Requester):
    def post(self, bank_transfer_request: BankTransferRequest) -> BankTransferResponse | Response:
        url = f'{self.base_url}/account/transfer'
        response = requests.post(
            url=url,
            json=bank_transfer_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return BankTransferResponse(**response.json())
        return response