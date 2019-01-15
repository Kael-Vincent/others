from flask_restful import Resource,reqparse
# from ..models.deal import Deal
from app_repr.models.base import db
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument('user_id',type=int)
parser.add_argument('book_id',type=int)


# class Deals(Resource):
#     def post(self):
#         args = parser.parse_args()
#         deal = Deal()
#         deal.set_attrs(args)
#         db.session.add(deal)
#         db.session.commit()
#         return jsonify({'code':0,'msg':'交易成功！'})