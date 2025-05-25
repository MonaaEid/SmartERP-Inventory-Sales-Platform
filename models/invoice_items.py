from sqlalchemy import Column, Integer, DateTime, ForeignKey

from models import Base
from datetime import datetime

class Invoice_Items(Base):
    """Invoice_Items model."""
    __tablename__ = "invoice_items"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)