from texttable import Texttable
def create_coffe_shop(name, country, price):
    return {
        'name': name,
        'country': country,
        'price': price,
    }

def get_name(a):
    return a['name']
def get_country(a):
    return a['country']
def get_price(a):
    return a['price']

def set_name(a, x):
    a['name'] = x
def set_country(a, x):
    a['country'] = x
def set_price(a, x):
    a['price'] = x

def add_coffe(shops, name, country, price):
    if price < 0:
        raise ValueError("Invalid price")
    shops.append(create_coffe_shop(name, country, price))

def show(shops):
    table = Texttable()
    table.header(["Name", "Country", "Price"])
    table.set_cols_align(["c", "c", "c"])

    shops_sorted = sorted(shops, key = lambda x: (get_country(x), get_price(x)))

    for shop in shops_sorted:
        table.add_row([get_name(shop), get_country(shop), get_price(shop)])

    return table

def filter_coffe(shops, country, price):
    table = Texttable()
    table.header(["Name", "Country", "Price"])
    table.set_cols_align(["c", "c", "c"])
    found = False
    coffes = []
    if country == None:
        coffes = shops.copy()

    else:
        for shop in shops:
            if get_country(shop) == country:
                coffes.append(shop)

    if price == None:
        for coffe in coffes:
            table.add_row([get_name(coffe), get_country(coffe), get_price(coffe)])
            found = True

    else:
        if price < 0:
            raise ValueError("Invalid price")

        for coffe in coffes:
            if get_price(coffe) <= price:
                table.add_row([get_name(coffe), get_country(coffe), get_price(coffe)])
                found = True

    return table, found