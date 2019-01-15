"""
created by Vincent
"""
from flask import Blueprint
from flask_restful import Api
from app_repr.api_repr.RegisterAndLoginApi import Register,Login
from app_repr.api_repr.IdCardApi import GetCardNo
from app_repr.api_repr.UploadRepaymentApi import UploadRepay
from app_repr.api_repr.addbook import AddBook
from app_repr.api_repr.WriteArticle import WriteArticle
# from .deal import Deals

api_bp = Blueprint('api_bp',__name__)
api = Api(api_bp)
api.add_resource(Register,'/register')
api.add_resource(Login,'/login')
api.add_resource(GetCardNo,'/get_nu')
api.add_resource(UploadRepay,'/upload')
api.add_resource(AddBook,'/addbook')
# api.add_resource(Deals,'/deal')
api.add_resource(WriteArticle,'/write_article')
