from pydantic import BaseModel

from enum import Enum

class Customer(BaseModel):
    id:int
    name:str
    contact_info:str
    address:str
    
class Order(BaseModel):
    id:int
    order_data:str
    customer:str
    total_amount:int