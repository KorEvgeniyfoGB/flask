# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа

from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Genre(BaseModel):
    id: int
    title: str


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str]
    genre: Genre


movies = [Movie(id=1, title="Terminator", description="film about....", genre=Genre(id=1, title="фантастика")),
          Movie(id=2, title="clue", description="comedy about..", genre=Genre(id=2, title="Комедия"))]


@app.get("/films", response_model=list[Movie])
async def get_movies(id_genre: int):
    my_movies = [i for i in movies if i.genre.id == id_genre]
    return my_movies


@app.get("/")
async def get_main():
    return "Movie base"


if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,
                reload=True)
