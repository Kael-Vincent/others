"""
create by Vincent on 2018-7-10
"""
from flask import Flask

__author__='Vincent'


def create_app():
    app = Flask(__name__)
    # app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from views.RegisterLoginApi import bluep
    app.register_blueprint(bluep)
