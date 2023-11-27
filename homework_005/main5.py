# Необходимо создать API для управления списком пользователей.
# Создайте класс User с полями id, name, email и password.

# API должен содержать следующие конечные точки:
# — GET /users — возвращает список пользователей.
# — GET /users/{id} — возвращает пользователя с указанным идентификатором.
# — POST /users — добавляет нового пользователя.
# — PUT /users/{id} — обновляет пользователя с указанным идентификатором.
# — DELETE /users/{id} — удаляет пользователя с указанным идентификатором.

# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
# Для этого использовать библиотеку Pydantic.


from faker import Faker
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, HTTPException, Request
import uvicorn
from fastapi.templating import Jinja2Templates


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str


class UserInp(BaseModel):
    name: str
    email: EmailStr
    password: str


app = FastAPI()
templates = Jinja2Templates(directory="templates")

fake = Faker('ru_RU')

users = [User(id=i, name=fake.name(), email=fake.email(),
              password=fake.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True))
         for i in range(10)]


@app.get("/", response_model=str)
async def main_page():
    return "Hello всем"


@app.get("/users", response_model=list[User])
async def get_users():
    return users


@app.get('/users{user_id}', response_model=User)
async def one_user(request: Request, user_id: int):
    if len(users) < user_id:
        raise HTTPException(status_code=404, detail='User not found')
    for i in users:
        if i.id == user_id:
            return i


# Возвращает страницу
# @app.get("/users{user_id}", response_class=HTMLResponse)
# async def whatsup_user(request: Request, user_id: int):
#     for i in users:
#         if i.id == user_id:
#             return templates.TemplateResponse(name="user.html", context={"request": request, 'user_id': i.name})


@app.put('/users{user_id}', response_model=User)
async def edit_user(user_id: int, new_user: UserInp):
    for user in users:
        if user.id == user_id:
            user.name = new_user.name
            user.email = new_user.email
            user.password = new_user.password
            return user
    raise HTTPException(status_code=404, detail='User not found')


@app.delete('/users{user_id}', response_model=str)
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return 'User удален'
    raise HTTPException(status_code=404, detail='Task not found')


if __name__ == '__main__':
    uvicorn.run('main5:app',
                host='127.0.0.1',
                port=8000,
                reload=True)
