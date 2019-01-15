from .base import Base
from sqlalchemy import Column,Integer,Time,DateTime
from datetime import datetime
from .book import Book
from .user import Users


# #交易表
# class Deal(Base):
#     __tablename__ = 'deal'
#     id =Column(Integer,primary_key=True)
#     user_id = Column(Integer,ForeignKey='user.id',nullable=False)
#     book_id = Column(Integer,nullable=False)
#     create_time = Column(DateTime,default=datetime.now)