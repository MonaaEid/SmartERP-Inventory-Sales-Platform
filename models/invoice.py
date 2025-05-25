from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import Base
from datetime import datetime

class Invoice(Base):
    """Invoice model."""
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(128), nullable=False)
    total_price = Column(Integer, nullable=False)
    invoice_items = relationship('Invoice_Items', backref='Invoice')

    created_at = Column(DateTime, default=datetime.utcnow)