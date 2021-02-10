from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_app(app_name, config_object):
    app = Flask(app_name)
    app.config.from_object(config_object)
    db.init_app(app)
    from .routes import app_routes
    app.register_blueprint(app_routes)
    return app

