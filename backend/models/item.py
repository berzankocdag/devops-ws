from sqlalchemy import Column, Integer, String
from db.base_class import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
