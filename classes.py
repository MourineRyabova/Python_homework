from pydantic import BaseModel
from datetime import datetime

class Item(BaseModel):
    index: int
    name: str
    price: int

class Store(BaseModel):
    index: int
    address: str

class Sales(BaseModel):
    index: int
    sale_time: datetime
    item_id: int
    store_id: int

class SalesIn(BaseModel):
    index: int
    sale_time: datetime
    item_id: int
    store_id: int

class TopStores(BaseModel):
    store_id: int
    address: str
    revenue: int

class TopItems(BaseModel):
    item_id: int
    name: str
    quantity: int