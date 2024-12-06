from sqlalchemy import Integer, String,PrimaryKeyConstraint,UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from data_base.data_base import Base

class Customer(Base):
    __tablename__ = "Customer"
    id:Mapped[int]=mapped_column(primary_key=True,nullable=False,autoincrement=True)
    name:Mapped[str]=mapped_column(nullable=False,unique=True)
    contact_info:Mapped[str]=mapped_column(nullable=False)
    address:Mapped[str]=mapped_column(nullable=False)
    
class Orders(Base):
    __tablename__="Orders"
    id:Mapped[int]=mapped_column(primary_key=True,nullable=False,autoincrement=True)
    order_data:Mapped[str]=mapped_column(nullable=False)
    customer:Mapped[str]=mapped_column(nullable=False)
    total_amount:Mapped[int]=mapped_column(nullable=False)
    
class OrderDetalis(Base):
    __tablename__ = "OrderDetalis"
    id:Mapped[int]=mapped_column(primary_key=True,nullable=False,autoincrement=True)
    order_id:Mapped[int]=mapped_column(nullable=False)
    product:Mapped[str]=mapped_column(nullable=False)
    quantity:Mapped[int]=mapped_column(nullable=False)#Количество заказов
    price:Mapped[int]=mapped_column(nullable=False)

class Products(Base):
    __tablename__ = "Products"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True, nullable=False)
    name:Mapped[str]=mapped_column(nullable=False)
    type:Mapped[str]=mapped_column(nullable=False)
    material:Mapped[str]=mapped_column(nullable=False)
    price:Mapped[int]=mapped_column(nullable=False)
    stocl_quantity:Mapped[int]=mapped_column(nullable=False)
    
class Suppliers(Base):
    __tablename__="Suppliers"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True, nullable=False)
    name:Mapped[str]=mapped_column(nullable=False)
    contact_info:Mapped[str]=mapped_column(nullable=False)
    product_id:Mapped[int]=mapped_column(nullable=False)
    