from flask_restful import Resource
from app_repr.util.pro_cardno import pro_card_no
from flask_login import login_required


class GetCardNo(Resource):
    # @login_required
    def get(self):
        cardNo = pro_card_no()
        return cardNo