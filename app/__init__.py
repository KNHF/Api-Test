# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(level=logging.DEBUG)


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    logging.debug("Flask app initialized")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    db.init_app(app)

    with app.app_context():
        from . import main
        app.register_blueprint(main.bp)

        db.create_all()

    return app
