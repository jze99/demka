from pydantic import BaseModel

from enum import Enum

class Customer(BaseModel):
    id:int
    name:str
    contact_info:str
    address:str