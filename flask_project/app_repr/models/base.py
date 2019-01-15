from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,SmallInteger
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
bs = declarative_base()


class Base(db.Model,bs):
    __abstract__=True
    # create_time = Column('create_time',Integer)
    status = Column('status',SmallInteger,default=1)

    def set_attrs(self, attrs_dict):
        for k, v in attrs_dict.items():
            if hasattr(self,k) and k != id:
                setattr(self, k, v)

