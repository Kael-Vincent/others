from flask import Flask,Response,Blueprint
from views.models.database import db_session,init_db,engine
from views.models.models import User

api = Blueprint('api',__name__)


@api.route('/',methods=['POST'])
def insert():
    init_db()
    u=User('idd','aabcnd@ww.com','123abc')
    if User.query.filter_by(name='d'):
        return 'd is exist'
    else:
        db_session.add(u)
        db_session.commit()
        return Response(u.name)


@api.route('/hello')
def hello():
    init_db()
    return 'hello world'


@api.teardown_request
def shutdown_session(exception=None):
    db_session.remove()



