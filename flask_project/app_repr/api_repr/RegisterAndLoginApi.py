"""
created by Vincent on 2018-7-13
# """
from flask_restful import reqparse, Resource
from app_repr.models.user import Users
from flask_login import login_user,login_required
from app_repr.models.base import db
from flask import jsonify,g
parse = reqparse.RequestParser()
parse.add_argument('username',type=str)
parse.add_argument('password',type=str)
parse.add_argument('email',type=str)

@login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })


class Register(Resource):
    def post(self):
        args = parse.parse_args()
        user=Users()
        if len(args.username)>80:
            return '用户名过长'
        elif user.query.filter_by(username=args['username']).first():
            return ('用户名已经存在,请重新输入！')
        else:
            user.set_attrs(args)
            db.session.add(user)
            db.session.commit()
            return '注册成功',200

    def get(self):
        return 'hello,world!'


class Login(Resource):
    def post(self):
        args = parse.parse_args()
        user = Users.query.filter_by(username=args.username).first()
        if user and user.check_password(args.password):
            login_user(user)
            token = user.generate_auth_token()
            return jsonify({'msg':'login successfully','token':token.decode('ascii')})
        else:
            return '账号或密码错误'
            # flash('账号或密码错误')
    # @api.teardown_request
    # def shutdown_session(exception=None):
    #     db.session.remove()






