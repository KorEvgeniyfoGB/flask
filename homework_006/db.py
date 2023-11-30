from settings import settings
import databases
import sqlalchemy

# пользователей должна содержать id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.

# заказов должна содержать id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY),
# дата заказа и статус заказа.

# товаров должна содержать id (PRIMARY KEY), название, описание и цена.
DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(32)),
    sqlalchemy.Column("lastname", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(256))
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("id_users", sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column("id_products", sqlalchemy.ForeignKey('products.id')),
    sqlalchemy.Column("data_order", sqlalchemy.String()),
    sqlalchemy.Column("status", sqlalchemy.BOOLEAN)
)

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("price", sqlalchemy.Float(20))
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)