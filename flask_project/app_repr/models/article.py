from .base import Base
from sqlalchemy import Integer,Column,DateTime,String,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True)
    choice_type = {1:'杂记',2:'电影',3:'摄影',4:'书籍'}
    create_time = Column(DateTime,default=datetime.now())
    title = Column(String(100),nullable=True)
    type = Column(String(10),nullable=False)
    content = Column(String(1000),nullable=False)
    images = Column(String(1000),nullable=True)
    user = relationship('Users')
    user_id = Column(Integer, ForeignKey('user.id'))