"""
created by Vincent on 2018-7-13
"""
from flask_login import LoginManager
from flask import Flask
from .models.base import db
from .api_repr import api_bp

login_manager = LoginManager()
app = Flask(__name__)
app.config.from_object('app_repr.settings')
app.config.from_object('app_repr.secure')
app.config['SQLALCHEMY_DATABASE_URI']


def create_app():
    # app = Flask(__name__)
    # app.config.from_object('app_repr.settings')
    # app.config.from_object('app_repr.secure')
    # app.config['SQLALCHEMY_DATABASE_URI']
    # print(app.config['SECRET_KEY'])
    db.init_app(app)
    db.create_all(app=app)
    login_manager.init_app(app)
    from app_repr.api_repr import api_bp
    app.register_blueprint(api_bp)
    return app


# @api.teardown_request
# def shutdown_session(exception=None):
#     db.session.remove()
#
# # def register_blueprint(app):
# #     from app_repr.api_repr import api_bp
# #     app.register_blueprint(api_bp)


