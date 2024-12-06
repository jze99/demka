from fastapi import APIRouter, Query, HTTPException
from data_base.qery import QeryDataBase
from data_base.models import main_models as mm
from model_messege import Customer
from typing import List
import yaml

router = APIRouter(prefix="/api-demka")

#table_name: mm.TableName = Query(...)

def parse_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data
    
@router.post("/start")
async def start():
    file_path = './api/test_data.yaml'
    parsed_data = parse_yaml(file_path)
    QeryDataBase.create_table(data=parsed_data)
    return {"log": "базы созданы"}

@router.post("/select",response_model=List[Customer])
async def select_table():
    data = QeryDataBase.select_table(mm.Customer)
    customers = []
    for customer in data:
        customers.append(
            Customer(
                id=customer._data[0].id,
                contact_info=customer._data[0].contact_info,
                address=customer._data[0].address
            )
        )
    return {"messeg": customers}

@router.post("/login")
async def login(auth_request:str):
    
    return {"exists": auth_request}