from sqlalchemy import Column, Integer, String, Float, DateTime
from .db import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)