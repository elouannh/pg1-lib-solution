""" Routes for the endpoint 'book'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.auth.models import AuthModel
from data.auth.schemas import AuthSchema
from shared import db

NAME = 'auth'

auth_blueprint = Blueprint(f"{NAME}_auth_blueprint", __name__)


@auth_blueprint.get(f"/{NAME}/<int:id>")
def get_auth(id: str):
    """GET route code goes here"""
    entity: AuthModel = db.session.query(AuthModel).get(id)
    if entity is None:
        return "Goodbye, World.", 404
    return entity.message, 200


@auth_blueprint.post(f"/{NAME}/")
def post_auth():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: AuthModel = AuthModel().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid AuthModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return AuthModel().dump(entity), 200


@auth_blueprint.delete(f"/{NAME}/<int:id>")
def delete_auth(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@auth_blueprint.put(f"/{NAME}/<int:id>")
def put_auth(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@auth_blueprint.patch(f"/{NAME}/<int:id>")
def patch_auth(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
