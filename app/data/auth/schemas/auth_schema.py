"""Schema for serializing/deserializing a BorrowBookModel"""

from data.auth.models.auth_model import AuthModel
from shared.utils.schema.base_schema import BaseSchema


class AuthSchema(BaseSchema):
    class Meta:
        model = AuthModel
        load_instance = True
