import pytest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_secret_request import CreateUserSecretRequest
from src.main.api.models.login_user_request import LoginUserRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_user_secret_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserSecretRequest)
    api_manager.admin_steps.create_user_secret(user_request)
    return user_request

@pytest.fixture
def login_user_request(api_manager):
    user_request = RandomModelGenerator.generate(LoginUserRequest)
    api_manager.admin_steps.login_user(user_request)
    return user_request














