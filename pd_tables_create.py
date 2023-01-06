import pandas as pd
import os
import random
from random import randrange
from datetime import timedelta
from datetime import datetime

def create_stores_table():
    stores = pd.read_csv(os.path.join(os.path.dirname(__file__), "stores_addresses.csv"), sep = '/n', header = None, engine='python')
    stores = stores.rename(columns = {0:'address'})
    stores = stores.reset_index()
    stores = stores.rename(columns = {'index':'id'})
    return stores

def create_items_table():
    items = pd.read_csv(os.path.join(os.path.dirname(__file__), "items.csv"), sep = '/n', header = None, engine='python')
    items = items.rename(columns = {0:'name'})
    items['price'] = random.sample(range(1, 100), len(items))
    items.reset_index(inplace=True)
    items = items.rename(columns = {'index':'id'})
    return items

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def create_sales_table():
    sales = pd.DataFrame()
    dates = []
    d1 = datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2023 4:50 AM', '%m/%d/%Y %I:%M %p')
    for i in range(1,1000):
        dates.append(random_date(d1, d2))
    sales['sale_time'] = dates
    item_ids = []
    for i in range (1, 1000):
        item_ids.append(random.randint(0, len(create_items_table())))
    sales['item_id'] = item_ids

    store_ids = []
    for i in range (1, 1000):
        store_ids.append(random.randint(0, len(create_stores_table())))
    sales['store_id'] = store_ids
    sales.reset_index(inplace=True)
    sales = sales.rename(columns = {'index':'id'})
    #sales['sale_time'] = pd.to_datetime(sales['sale_time'], unit='D')
    sales = sales.sort_values(by = 'sale_time')
    return sales