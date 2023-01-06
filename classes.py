from pydantic import BaseModel
from datetime import datetime

class Item(BaseModel):
    id: int
    name: str
    price: int

class Store(BaseModel):
    id: int
    address: str

class Sales(BaseModel):
    id: int
    sale_time: datetime
    item_id: int
    store_id: int

class SalesIn(BaseModel):
    #id: int
    sale_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item_id: int
    store_id: int

class TopStores(BaseModel):
    period: str
    store_id: int
    address: str
    month_revenue: int

class TopItems(BaseModel):
    item_id: int
    name: str
    quantity: int