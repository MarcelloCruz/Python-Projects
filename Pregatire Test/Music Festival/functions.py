from texttable import Texttable

class Festival:
    def __init__(self, name, month, cost, artists_list):
        self.name = name
        self.month = month
        self.cost = cost
        self.artists_list = artists_list

def get_month(month):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November"]
    return months[month - 1]

def check_f(festivals, name, month):
    for names in festivals:
        if names.name == name:
            raise ValueError("The names already exist")

    if not(1 <= month <= 12):
        raise ValueError("Invalid month")

def add_festival(festivals, name, month, cost, artists_list):
    check_f(festivals, name, month)
    festivals.append(Festival(name, month, cost, artists_list))

def season_months(season):
    if season == "winter":  return [12,1,2]
    if season == "spring":  return [3,4,5]
    if season == "summer":  return [6,7,8]
    if season == "autumn":  return [9,10,11]

def show_season(festivals, season):
    table = Texttable()
    table.header(["Festival", "Month", "Cost", "Artists"])
    table.set_cols_align(["c", "c", "c", "c"])

    idx = season_months(season)

    copy1 = festivals.copy()
    copy1.sort(key = lambda festival: festival.month)
    copy2 = []
    for festival in copy1:
        if festival.month in idx:
            copy2.append(festival)

    copy2.sort(key = lambda festival: festival.name)
    for festival in copy2:
        table.add_row([festival.name, get_month(festival.month), festival.cost, festival.artists_list])

    return table

def show_artist(artists_list, artist_name):
    table = Texttable()
    table.header(["Festival", "Month", "Cost", "Artists"])
    table.set_cols_align(["c", "c", "c", "c"])

    copy1 = artists_list.copy()
    copy1.sort(key = lambda festival: festival.month)

    for festival in copy1:
        if artist_name in festival.artists_list:
            table.add_row([festival.name, get_month(festival.month), festival.cost, festival.artists_list])

    return table

def show_all(festivals):
    table = Texttable()
    table.header(["Festival", "Month", "Cost", "Artists"])
    table.set_cols_align(["c", "c", "c", "c"])
    for festival in festivals:
        table.add_row([festival.name, get_month(festival.month), festival.cost, festival.artists_list])

    return table