from fastapi import APIRouter
from homework_006.models import Order, OrderIn, User, Product
from homework_006.db import users, products, orders, database
from datetime import datetime

router = APIRouter()


@router.get("/orders/", response_model=list[Order])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.get("/orders/{order_id}", response_model=Order | None)
async def one_orders(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@router.post("/orders/", response_model=str)
async def create_orders(order: OrderIn):
    query = orders.insert().values(
        id_users=order.id_users,
        id_products=order.id_products,
        data_order=order.data_order,
        status=order.status,
    )
    await database.execute(query)
    return f"Заказ добавлен"


@router.put("/orders/{order_id}")
async def edit_orders(order_id: int, new_order: OrderIn):
    query = (
        orders.update()
        .where(orders.c.id == order_id)
        .values(
            id_users=new_order.id_users,
            id_prodect=new_order.id_prodects,
            data_order=new_order.data_order,
            status=new_order.status,
        )
    )
    await database.execute(query)
    return f"Заказ изменен"


@router.delete("/orders/{order_id}")
async def del_orders(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return f"Заказ удален"