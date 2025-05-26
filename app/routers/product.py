from fastapi import APIRouter
from models.product import Product
from ..dependencies import SessionDep

router = APIRouter(
    prefix="/products",
    tags=["products"],
    # dependencies=[Depends(SessionDep)],
    responses={404: {"description": "Not found"}},
)



@router.post("/create_product")
def create_product(name: str, price: float,
                   session: SessionDep,) -> dict[str, str]:
    """Create a new product."""
    new_product = Product(name=name, price=price)
    session.add(new_product)
    session.commit()
    return {"message": "Product created successfully."}
