import logging
import os
import sys

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

db: SQLAlchemy = SQLAlchemy()
migrate = Migrate()


def create_app(config):
    app = Flask(__name__)
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    app.config.from_object(config)
    print(f"Using {app.config['DB_NAME']}")

    db.init_app(app)
    if app.config['MIGRATION'] == "1":
        migrate.init_app(app, db)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    url_prefix = "/api"

    from data.book.controllers import book_blueprint
    from data.auth.controllers import login_blueprint
    from data.auth.controllers import register_blueprint
    app.register_blueprint(book_blueprint, url_prefix=url_prefix)
    app.register_blueprint(login_blueprint, url_prefix=url_prefix)
    app.register_blueprint(register_blueprint, url_prefix=url_prefix)

    @app.errorhandler(ValidationError)
    def handle_custom_error(error):
        return str(error), 400

    CORS(app, resources={r"/*": {"origins": "*"}})

    with app.app_context():
        db.create_all()

    return app
