""" Routes for the endpoint 'login'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.auth.models import AuthModel
from data.auth.schemas import AuthSchema
from shared import db

NAME = 'login'

login_blueprint = Blueprint(f"{NAME}_auth_blueprint", __name__)


@login_blueprint.get(f"/{NAME}/<int:id>")
def get_login(id: str):
    """GET route code goes here"""
    entity: AuthModel = db.session.query(AuthModel).get(id)
    if entity is None:
        return "Goodbye, World.", 404
    return entity.message, 200


@login_blueprint.post(f"/{NAME}/")
def post_login():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: AuthModel = AuthModel().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid AuthModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return AuthModel().dump(entity), 200


@login_blueprint.delete(f"/{NAME}/<int:id>")
def delete_login(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@login_blueprint.put(f"/{NAME}/<int:id>")
def put_login(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@login_blueprint.patch(f"/{NAME}/<int:id>")
def patch_login(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
