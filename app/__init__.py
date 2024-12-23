# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # Using SQLite for simplicity
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    db.init_app(app)

    with app.app_context():
        from . import main
        app.register_blueprint(main.bp)

        db.create_all()

    return app
