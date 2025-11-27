from readline import set_pre_input_hook
from texttable import Texttable

def create_phone(manuf, model, price):
    return {
        'manuf' : manuf,
        'model' : model,
        'price' : price
    }

def get_manuf(a):
    return a['manuf']
def get_model(a):
    return a['model']
def get_price(a):
    return a['price']

def set_manuf(a, x):
    a['manuf'] = x
def set_model(a, x):
    a['model'] = x
def set_price(a, x):
    a['price'] = x

def add_phone(phones, manuf, model, price):
    if len(manuf) < 3 or len(model) < 3 or len(str(price)) < 3:
        raise Exception("All inputs must have at least 3 characters")

    phones.append(create_phone(manuf, model, price))


def find_phone(phones, manuf):
    table = Texttable()
    table.header(["Manufacturer", "Model", "Price"])
    table.set_cols_align(['c', 'c', 'c'])

    for phone in phones:
        if manuf in get_manuf(phone):
            table.add_row([get_manuf(phone), get_model(phone), get_price(phone)])

    return table

def shw_all(phones):
    table = Texttable()
    table.header(["Manufacturer", "Model", "Price"])
    table.set_cols_align(['c', 'c', 'c'])
    for phone in phones:
        table.add_row([get_manuf(phone), get_model(phone), get_price(phone)])

    return table

def increase_price(phones,manuf, model, price):
   found = False

   for phone in phones:
       if manuf == get_manuf(phone) and model == get_model(phone):
           set_price(phone, get_price(phone) + price)
           found = True
           break

   if not found:
        raise ValueError("The phone is missing")

def increase_percentage(phones, percentage):
    if not(-50 <= percentage <= 100):
        raise ValueError("The percentage is invalid")

    for phone in phones:
        set_price(phone, get_price(phone) * (1 + percentage / 100))
