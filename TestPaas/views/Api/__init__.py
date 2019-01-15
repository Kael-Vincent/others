from flask import Flask
from flask import Blueprint

"""
created by Vincent
"""


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from views.Api.Register import api
    app.register_blueprint(api)