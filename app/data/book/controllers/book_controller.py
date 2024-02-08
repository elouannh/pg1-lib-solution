""" Routes for the endpoint 'book'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.book.models import BookModel
from data.book.schemas import BookSchema
from shared import db

NAME = 'book'

book_blueprint = Blueprint(f"{NAME}_book_blueprint", __name__)


@book_blueprint.get(f"/{NAME}/<int:id>")
def get_book(id: str):
    """GET route code goes here"""
    entity: BookModel = db.session.query(BookModel).get(id)
    if entity is None:
        return "Goodbye, World.", 404
    return entity.message, 200


@book_blueprint.post(f"/{NAME}/")
def post_book():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: BookModel = BookModel().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid HelloWorldModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return BookModel().dump(entity), 200


@book_blueprint.delete(f"/{NAME}/<int:id>")
def delete_book(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@book_blueprint.put(f"/{NAME}/<int:id>")
def put_book(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@book_blueprint.patch(f"/{NAME}/<int:id>")
def patch_book(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
