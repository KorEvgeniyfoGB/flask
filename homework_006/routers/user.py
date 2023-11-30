from fastapi import APIRouter
from homework_006.models import User, UserIn
from homework_006.db import users, database
from sqlalchemy import or_

router = APIRouter()


@router.get("/users/", response_model=list[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/searchname/{user_firstname}", response_model=list[User] | None)
async def one_user(user_firstname: str):
    query = users.select().filter(or_(users.c.firstname == user_firstname, users.c.lastname == user_firstname))
    return await database.fetch_all(query)


@router.get("/users/searchid/{user_id}", response_model=User | None)
async def one_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@router.post("/users/", response_model=str)
async def create_user(user: UserIn):
    query = users.insert().values(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=user.password,
    )
    await database.execute(query)
    return f"Пользователь {user.id} добавлен"


@router.put("/users/{user_id}")
async def edit_user(user_id: int, new_user: UserIn):
    query = (
        users.update()
        .where(users.c.id == user_id)
        .values(
            firstname=new_user.firstname,
            lastname=new_user.lastname,
            email=new_user.email,
            password=new_user.password,
        )
    )
    await database.execute(query)
    return f"Пользователь {user_id} изменен"


@router.delete("/users/{user_id}")
async def del_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return f"Пользователь {user_id} удален"
