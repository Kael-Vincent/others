from .base import Base
from sqlalchemy import Integer,Column,DateTime
from datetime import datetime


class Inventory(Base):
    id = Column(Integer,primary_key=True)
    book_id = Column(Integer,nullable=False)
    create_time = Column(DateTime,default=datetime.now())
    update_time = Column(DateTime,default=create_time,onupdate=True)