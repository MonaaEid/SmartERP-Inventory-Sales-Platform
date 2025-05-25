from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .user import User
from .product import Product
from .invoice import Invoice
from .invoice_items import Invoice_Items