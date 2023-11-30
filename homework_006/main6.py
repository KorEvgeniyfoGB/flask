from fastapi import FastAPI
import uvicorn
from db import database
from homework_006.routers import user, products, orders

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def index():
    return "Хотелось бы доработать, но время до срока осталось мало"

app.include_router(user.router, tags=['Users'])
app.include_router(products.router, tags=['Products']),
app.include_router(orders.router, tags=['Orders']),


if __name__ == '__main__':
    uvicorn.run("main6:app", host='127.0.0.1', port=8000, reload=True)
