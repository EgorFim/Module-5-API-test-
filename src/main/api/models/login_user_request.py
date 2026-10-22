from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel


class LoginUserRequest(BaseModel):
    username: Annotated[str, CreationRule(regex='^admin')]
    password: Annotated[str, CreationRule(regex=r'^123456')]
