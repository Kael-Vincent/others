from flask import Flask,Blueprint
from flask_restful import reqparse, Api, Resource
from views.models.database import db_session
from views.models.models import User
from werkzeug.security import generate_password_hash
import json,requests,time
from views import create_app
bluep = Blueprint('bluep',__name__)

api = Api(bluep)
parse = reqparse.RequestParser()
parse.add_argument('username', type=str)
parse.add_argument('passwd', type=str)
parse.add_argument('email', type=str)


class Register(Resource):

    def post(self):
        args = parse.parse_args()
        # User.set_attrs(self,args)
        passwd = generate_password_hash(args.passwd)
        username = args.username
        email = args.email
        if User.query.filter_by(name=username).first():
             return ('用户已存在')
        else:
             u = User(email, username, passwd)
             db_session.add(u)
             db_session.commit()
             return ('注册成功'),

    @bluep.teardown_request
    def shutdown_session(exception=None):
        db_session.remove()


class Login(Resource):

    def post(self):
        args = parse.parse_args()
        User.set_attrs(args)
        # self.username = args.username
        user = User.query.filter_by(name=self.username).first()
        pd = User.query.filter_by(passwd=self.passwd).first()
        if user != None and pd !=None:
            return ('登录成功！')
        else:
            return ('密码或账号错误，请重新输入！')

    @bluep.teardown_request
    def shutdown_session(exception=None):
        db_session.remove()


# bluep.add_resource(Register,'/register')
api.add_resource(Login,'/login')


if __name__ == '__main__':
    bluep.run()