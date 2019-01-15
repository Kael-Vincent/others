""""
created by Vincent on 2018-7-16
"""
from sqlalchemy import Column, Integer, String,DateTime
from werkzeug.security import generate_password_hash,check_password_hash
from .base import Base
from flask_login import UserMixin#调用返回get_id()
from itsdangerous import SignatureExpired,BadSignature, TimedJSONWebSignatureSerializer as Serializer
from app_repr.secure import SECRET_KEY
from datetime import datetime


class Users(UserMixin,Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=False, nullable=False)
    email = Column(String(120), unique=False, nullable=False)
    _password = Column('password',String(200),unique=False,nullable=False)
    create_time = Column(DateTime,default=datetime.now())

    @property
    def password(self):
        # print('调用getter')
        return self._password

    # 设置密码
    @password.setter
    def password(self, raw):
        # print('调用setter！')
        self._password = generate_password_hash(raw)

    # 检查密码登录
    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def generate_auth_token(self, expiration=600):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = Users.query.get(data['id'])
        return user





