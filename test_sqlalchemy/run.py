"""
created by Vincent on 2018-7-13
# """
from flask_restful import reqparse, Resource,Api
from flask import Flask
from helloworld.view.hello import Users
app = Flask(__name__)
api = Api(app)
parse = reqparse.RequestParser()
parse.add_argument('username',type=str)
parse.add_argument('password',type=str)
parse.add_argument('email',type=str)


class Register(Resource):
    def post(self):
        args = parse.parse_args()
        user=Users()
        user.set_attrs(args)
        print(user._password)

    def get(self):
        return 'hello,world!'

    # @api.teardown_request
    # def shutdown_session(exception=None):
    #     db.session.remove()


api.add_resource(Register,'/register')


if __name__=='__main__':
    app.run(debug=False)

