"""Schema for serializing/deserializing a BorrowBookModel"""

from data.book.models.book_model import BookModel
from shared.utils.schema.base_schema import BaseSchema


class BookSchema(BaseSchema):
    class Meta:
        model = BookModel
        load_instance = True
