from sqlalchemy import Column, Integer, String,ForeignKey
from .base import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__='book'
    id = Column(Integer,primary_key=True)
    name = Column(String(120),nullable=False)
    publisher = Column(String(120),nullable=False)
    price = Column(Integer,nullable=False)
    image = Column(String(50))
    author = Column(String(20),default='佚名')
    pages = Column(Integer,nullable=False)
    user = relationship('Users')
    owner_id = Column(Integer,ForeignKey('user.id'))