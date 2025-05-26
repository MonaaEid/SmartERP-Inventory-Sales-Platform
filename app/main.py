from fastapi import FastAPI, Depends


from fastapi.middleware.cors import CORSMiddleware
from .routers import invoice, product
from models import Base
from app.database import engine

app = FastAPI()

app.include_router(invoice.router)
app.include_router(product.router)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    # allow_headers=["*"],
)

@app.on_event ("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello"}


# About page route
@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}



if __name__ == "__main__":
    # Run the FastAPI app using uvicorn
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
