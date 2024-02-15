from typing import Final
import os
import binascii


class BaseConfig:
    """Configuration common to all modes (test, dev, prod)"""

    def __init__(self):
        # Flask
        self.MIGRATION: Final[str] = os.getenv("MIGRATION")

        # Tokenization
        secret_key = binascii.hexlify(os.urandom(32)).decode('utf-8')
        self.JWT_SECRET_KEY = secret_key

        # Database
        self.USER: Final[str] = os.getenv("DB_USER")
        self.DB_PASS: Final[str] = os.getenv("DB_PASS")
        self.DB_NAME: Final[str] = os.getenv("DB_NAME")
        self.DB_IP: Final[str] = os.getenv("DB_IP")
        self.SQLALCHEMY_DATABASE_URI: Final[str] = \
            f"postgresql://{self.USER}:{self.DB_PASS}@{self.DB_IP}:5432/{self.DB_NAME}"


class TestingConfig(BaseConfig):
    def __init__(self):
        super().__init__()
        self.DEBUG = True
        self.ENV = "test"


class DevelopmentConfig(BaseConfig):
    def __init__(self):
        super().__init__()
        self.DEBUG = True
        self.ENV = "dev"


class ProductionConfig(BaseConfig):
    def __init__(self):
        super().__init__()
        self.DEBUG = False
        self.ENV = "prod"
