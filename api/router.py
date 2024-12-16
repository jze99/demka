from fastapi import APIRouter, Query, HTTPException
from data_base.qery import QeryDataBase
from data_base.models import main_models as mm
from model_messege import Customer, Order
from typing import List
import yaml

router = APIRouter(prefix="/api-demka")



def parse_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data
    
@router.post("/start")
async def start():
    file_path = './test_data.yaml'
    parsed_data = parse_yaml(file_path)
    QeryDataBase.create_table(data=parsed_data)
    return {"log": "базы созданы"}

@router.post("/select", response_model=List[Customer])
async def select_table():
    data = QeryDataBase.select_table(mm.Customer)
    customers = []
    
    for customer in data:
        customers.append(
            Customer(
                id=customer[0].id,
                name=customer[0].name,
                contact_info=customer[0].contact_info,
                address=customer[0].address
            )
        )
    return customers

@router.post("/add", response_model=dict)
async def add_customer(customer: Customer):
    if not customer.name or not customer.contact_info or not customer.address:
        return{"message":"Заполнены не все поля"}
    response_message = QeryDataBase.add_customer(customer)
    return response_message 

@router.post("/update", response_model=dict)
async def update_customer(customer: Customer):
    if not customer.name or not customer.contact_info or not customer.address:
        return{"message":"Заполнены не все поля"}
    response_message = QeryDataBase.update_customer(customer_id=customer.id, updated_data=customer)
    return response_message

@router.post("/delete", response_model=dict)
async def delete_customer(customers: List[Customer]):
    customer_ids = [customer.id for customer in customers]  # Извлечение ID из входящих данных
    response_message = QeryDataBase.delete_customers(customer_ids=customer_ids)
    return response_message




@router.post("/select1", response_model=List[Order])
async def select_table1():
    data = QeryDataBase.select_table(mm.Orders)
    orders = []
    
    for order in data:
        orders.append(
            Order(
                id=order[0].id,
                order_data=order[0].order_data,
                customer=order[0].customer,
                total_amount=order[0].total_amount
            )
        )
    return orders

@router.post("/add1", response_model=dict)
async def add_order(order: Order):
    if not order.order_data or not order.customer or not order.total_amount:
        return{"message":"Заполнены не все поля"}
    response_message = QeryDataBase.add_order(order=order)
    return response_message 

@router.post("/update1", response_model=dict)
async def update_order(order: Order):
    if not order.order_data or not order.customer or not order.total_amount:
        return{"message":"Заполнены не все поля"}
    response_message = QeryDataBase.update_order(order_id=order.id,data_order=order)
    return response_message

@router.post("/delete1", response_model=dict)
async def delete_order(orders: List[Order]):
    orders_ids = [order.id for order in orders]  # Извлечение ID из входящих данных
    response_message = QeryDataBase.delete_order(order_ids=orders_ids)
    return response_message