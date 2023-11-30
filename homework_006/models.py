from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Union
from datetime import datetime


class Product(BaseModel):
    id: int = Field(...)
    title: str = Field(..., min_length=2)
    description: str = Field(...)
    price: float = Field(..., gt=0, le=100000)


class ProductIn(BaseModel):
    title: str = Field(..., min_length=2)
    description: str = Field(..., max_length=1000)
    price: float = Field(..., gt=0, le=100000)


class User(BaseModel):
    id: int = Field(...)
    firstname: str = Field(..., max_length=50)
    lastname: str = Field(..., max_length=50)
    email: EmailStr = Field(..., max_length=128)
    password: str = Field(..., min_length=5)


class UserIn(BaseModel):
    firstname: str = Field(..., min_length=2)
    lastname: str = Field(..., min_length=2)
    email: str = Field(..., max_length=128)
    password: str = Field(..., min_length=5)


class Order(BaseModel):
    id: int = Field(...)
    id_users: int = Field(...)
    id_products: Union[int, list[int]] = Field(...)
    data_order: date = Field(..., format="%Y-%m-%d")
    status: bool = False


class OrderIn(BaseModel):
    id_users: int = Field(...)
    id_products: int = Field(...)
    data_order: date = datetime.now().strftime('%Y-%m-%d')
    status: bool = False


# a = Order(id=1, id_users=1, id_products=1, data_order=datetime.now().strftime('%Y-%m-%d'), status=True)
# print(a)