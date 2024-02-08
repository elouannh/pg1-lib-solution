from sqlalchemy import Column, String, Integer

from shared import db


class BookModel(db.Model):
    __tablename__ = "book"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    message = Column(String(100))
