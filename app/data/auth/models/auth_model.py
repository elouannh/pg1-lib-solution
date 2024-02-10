from sqlalchemy import Column, String, Integer

from shared import db


class AuthModel(db.Model):
    __tablename__ = "auth"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    message = Column(String(100))
