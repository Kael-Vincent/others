from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from .database import metadata, db_session
from werkzeug.security import generate_password_hash,check_password_hash


class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None,passwd=None):
        self.name = name
        self.email = email
        self.passwd = passwd

    def __repr__(self):
        return '<User %r>' % (self.name)

    # def set_attrs(self, attrs_dict):
    #     for k, v in attrs_dict.items():
    #         if hasattr(self,k) and k != id:
    #             setattr(self, k, v)
    #
    # @property
    # def passwd(self):
    #     return self.passwd
    #
    # # @passwd.setter
    # # def passwd(self, raw):
    # #         self.passwd = generate_password_hash(raw)
    #
    # def check_passwd(self,raw):
    #     return check_password_hash(self.passwd,raw)
    #
    # def get_id(self):
    #     return self.id


# users = Table('user', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(50), unique=True),
#     Column('email', String(120), unique=True),
#     Column('passwd',String(50))
#
# )
# mapper(User, users)
#


