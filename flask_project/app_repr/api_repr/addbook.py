from flask_restful import reqparse, Resource
from app_repr.models.book import Book
from app_repr.models.base import db
from flask import jsonify
from ..models.user import Users
parser = reqparse.RequestParser()
parser.add_argument('name',type=str)
parser.add_argument('publisher',type=str)
parser.add_argument('price',type=int)
parser.add_argument('image',type=str)
parser.add_argument('author',type=str)
parser.add_argument('pages',type=int)
parser.add_argument('user_id')
parser.add_argument('token',type=str,location='headers')


class AddBook(Resource):
    def post(self):
        user=Users()
        args = parser.parse_args()
        if user.verify_auth_token(args['token'])==None:
            return jsonify({'code':-1,'msg':'登录失效'})
        else:
            # value_is_none(args)
            for (k,v) in args.items():
                if v == None:
                    return jsonify({"msg":k+' '+'can not be null'})
                    # break
            book = Book()
            book.set_attrs(args)
            db.session.add(book)
            db.session.commit()
            return jsonify({'code':0,'msg':'successful'})








