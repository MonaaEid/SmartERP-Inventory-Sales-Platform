from fastapi import APIRouter
from models.invoice  import Invoice
from models.invoice_items import Invoice_Items
from ..dependencies import SessionDep
from typing import Annotated, List

router = APIRouter(
    prefix="/invoices",
    tags=["/invoices"],
    responses={404: {"description": "Not found"}},
)

def invoice_items(product_id: list[int], price: list[int], quantity: list[int]) -> tuple[list[Invoice_Items], int]:
    """Create a list of Invoice_Items objects and calculate total price."""
    items = []
    total_price = 0
    for i in range(len(quantity)):
        item = Invoice_Items(
            product_id=product_id[i],
            price=price[i],
            quantity=quantity[i]
        )
        items.append(item)
        total_price += price[i] * quantity[i]
    return items, total_price

@router.post("/create_invoice")
def create_invoice(customer_name: str,
                   product_id: list[int],
                   price: list[int],
                   quantity: list[int],
                   session: SessionDep) -> dict[str, str]:
    """Create a new invoice and its items in a single transaction."""
    items, total_price = invoice_items(product_id, price, quantity)
    new_invoice = Invoice(customer_name=customer_name, total_price=total_price)
    session.add(new_invoice)
    session.flush()
    for item in items:
        item.invoice_id = new_invoice.id
    session.add_all(items)
    session.commit()
    session.refresh(new_invoice)
    return {"message": "Invoice created successfully.", "invoice_id": str(new_invoice.id)}