import sqlite3
import databases
import pandas as pd
from pd_tables_create import create_stores_table, create_items_table, create_sales_table
from contextlib import closing
from fastapi import FastAPI
from typing import List

from classes import Item, Store, Sales, SalesIn, TopStores, TopItems 

def dict_factory(cursor, row):
    """Row factory для представления результатов в виде словаря."""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

SQLITE_FILE = "toys.db"
SQLITE_DSN = f"sqlite:///{SQLITE_FILE}"
database = databases.Database(SQLITE_DSN)

with sqlite3.connect(SQLITE_FILE) as conn: # соединение
    conn.row_factory = dict_factory # указать функцию для преобразования результатов select-запроса (не обязательно)
    with closing(conn.cursor()) as cursor: # область памяти для складывания результатов
        #Это 3 функции, которые выдают готовые таблицы для загрузки в базу
        create_stores_table().to_sql('store', conn, if_exists='replace', index=False, dtype={'id': 'INTEGER PRIMARY KEY',
                                    'address': 'STRING'})
        create_items_table().to_sql('item', conn, if_exists='replace', index=False, dtype={'id': 'INTEGER PRIMARY KEY',
                                    'name': 'STRING', 'price':'INTEGER'})
        create_sales_table().to_sql('sales', conn, if_exists='replace', index=False, dtype={'id': 'INTEGER PRIMARY KEY',
                                    'sale_time': 'DATETIME', 'item_id': 'INTEGER', 'store_id': 'INTEGER'})
        #подтверждение заливки в базу 
        #conn.commit()
        #sql = '''SELECT * FROM store LIMIT 5'''
        #cursor.execute(sql)
        #print(cursor.fetchall())

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/items/", response_model=List[Item])
async def get_items():
    query = '''SELECT * FROM toys.item LIMIT 5'''
    return await database.fetch_all(query)

@app.get("/stores/", response_model=List[Store])
async def get_stores():
    query = '''SELECT * FROM store LIMIT 5'''
    return await database.fetch_all(query)

"""@app.post("/sales/", response_model=Sales)
async def create_sale(sale: SalesIn):
    query = sales.insert().values(sale_time=datetime.now(), item_id=sale.item_id, store_id=sale.store_id)
    last_record_id = await database.execute(query)
    return {**sale.dict(), "id": last_record_id}"""

@app.get("/items/top_10", response_model=List[TopItems])
async def get_top_items():
    #топ 10 самых продаваемых товаров (id + наименование + количество проданных товаров)
    query = '''SELECT s.item_id as item_id,
                        i.name as name,
                        COUNT(DISTINCT s.sale_time) as quantity        
                 FROM sales s
                 JOIN item i ON s.item_id = i.id
                 GROUP BY item_id, name
                 ORDER BY quantity DESC, name
                 LIMIT 10;'''
    return await database.fetch_all(query)

@app.get("/stores/top_10", response_model=List[TopStores])
async def get_top_stores():
    query = ''''''
    return await database.fetch_all(query)