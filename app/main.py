from fastapi import FastAPI
from models import Base
from app.database import SessionLocal, engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.product import Product
from models.invoice import Invoice
from models.invoice_items import Invoice_Items

# Import all models so they are registered with SQLAlchemy's Base
import models.user, models.product, models.invoice, models.invoice_items

app = FastAPI()
Session = sessionmaker(bind=engine)
session = Session()

@app.post("/create_product", response_model=dict[str, str])
def create_product(name: str, price: float) -> dict[str, str]:
    """Create a new product."""
    new_product = Product(name=name, price=price)
    session.add(new_product)
    session.commit()
    return {"message": "Product created successfully."}

def root() -> dict[str, str]:
    return {"message": "Hello"}


# About page route
@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}



if __name__ == "__main__":
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    # Run the FastAPI app using uvicorn
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
