from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models import Base
from datetime import datetime

class Product(Base):
    """Product model."""
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), unique=True, index=True, nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, default=0)
    invoice_items = relationship('Invoice_Items', backref='product')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)