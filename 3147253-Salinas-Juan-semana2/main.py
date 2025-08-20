from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Mi API FastAPI - Semana 2",
    description="API con Type Hints, Pydantic y endpoints GET/POST",
    version="2.0.0"
)


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: Optional[bool] = True



products_db = [
    {"id": 1, "name": "Leche", "price": 21.000, "in_stock": True},
    {"id": 2, "name": "Huevos", "price": 13.000, "in_stock": True},
    {"id": 3, "name": "Arroz", "price": 52.000, "in_stock": False}
]


@app.get("/")
def home() -> dict:
    return {"message": "API FastAPI - Semana 2 funcionando "}


@app.get("/products")
def get_products() -> dict:
    return {"products": products_db}


@app.get("/products/{id}")
def get_product(id: int) -> dict:
    for product in products_db:
        if product["id"] == id:
            return {"product": product}
    return {"error": "Producto no encontrado"}

@app.post("/products")
def create_product(product: Product) -> dict:
    new_product = product.dict()
    products_db.append(new_product)
    return {"message": "Producto creado con éxito", "product": new_product}

@app.get("/search")
def search_products(name: str) -> dict:
    results = [p for p in products_db if name.lower() in p["name"].lower()]
    return {"results": results}
