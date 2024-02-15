""" Routes for the endpoint 'register'"""

from flask import Blueprint, request
from flask_bcrypt import Bcrypt
from marshmallow import ValidationError

from data.auth.models import AuthModel
from data.auth.schemas import AuthSchema
from shared import db

NAME = 'register'

register_blueprint = Blueprint(f"{NAME}_auth_blueprint", __name__)


@register_blueprint.get(f"/{NAME}/<int:id>")
def get_register(id: str):
    """GET route code goes here"""
    entity: AuthModel = db.session.query(AuthModel).get(id)
    if entity is None:
        return "Goodbye, World.", 404
    return entity.message, 200


@register_blueprint.post(f"/{NAME}/")
def post_register():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: AuthModel = AuthModel().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid AuthModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return AuthModel().dump(entity), 200


@register_blueprint.delete(f"/{NAME}/<int:id>")
def delete_register(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@register_blueprint.put(f"/{NAME}/<int:id>")
def put_register(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@register_blueprint.patch(f"/{NAME}/<int:id>")
def patch_register(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
