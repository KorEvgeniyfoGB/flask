from fastapi import APIRouter
from homework_006.models import Product, ProductIn
from homework_006.db import products, database
from sqlalchemy import or_


router = APIRouter()


@router.get("/products/", response_model=list[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/users/searchprodname/{product_name}", response_model=list[Product] | None)
async def search_name_product(product_name: str):
    query = products.select().filter(products.c.title == product_name)
    return await database.fetch_all(query)


@router.get("/products/searchprodid/{product_id}", response_model=Product | None)
async def one_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@router.post("/products/", response_model=str)
async def create_product(product: ProductIn):
    query = products.insert().values(
        title=product.title,
        description=product.description,
        price=product.price,
    )
    await database.execute(query)
    return f"Товар {product.title} добавлен"


@router.put("/products/{product_id}")
async def edit_product(product_id: int, new_product: ProductIn):
    query = (
        products.update()
        .where(products.c.id == product_id)
        .values(
            title=new_product.title,
            description=new_product.description,
            price=new_product.price,
        )
    )
    await database.execute(query)
    return f"Товар {product_id} изменен"


@router.delete("/products/{product_id}")
async def del_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return f"Товар {product_id} удален"


