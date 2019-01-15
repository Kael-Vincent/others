from flask_restful import reqparse,Resource
from app_repr.models.article import Article
from app_repr.models.base import db
from flask import jsonify
# from flask_login import login_required
from app_repr.models.user import Users
parse = reqparse.RequestParser()
parse.add_argument('user_id',type=str)
parse.add_argument('title',type=str)
parse.add_argument('type',type=str)
parse.add_argument('content',type=str)
parse.add_argument('images',type=str)
parse.add_argument('token',type=str,location='headers')


class WriteArticle(Resource):
    def post(self):
        args = parse.parse_args()
        artilce = Article()
        user = Users()
        # print(args)
        if user.verify_auth_token(args['token']) == None:
            return jsonify({'code': -1, 'msg': '登录失效'})
        else:
            for (k,v) in args.items():
                if v == None:
                    return jsonify({"msg":k+' '+'can not be null'})
                # continue
            else:
                artilce.set_attrs(args)
                db.session.add(artilce)
                db.session.commit()
                return jsonify({'code':0,'msg':'提交成功'})

