from texttable import Texttable as T

class Flights:
    def __init__(self, code, duration, departure_city, destination_city):
        self.code = code
        self.duration = duration
        self.departure_city = departure_city
        self.destination_city = destination_city

def add_flight(flights_list, code, duration, departure_city, destination_city):
    flights_list.append(Flights(code, duration, departure_city, destination_city))

def delete_flight(flights_list, code):
    for flight in flights_list:
        if flight.code == code:
            flights_list.remove(flight)

def show_flights(flights_list, vf):
    table = T()
    table.header(["Nr", "Code", "Duration", "Departure City", "Destination City"])
    table.set_cols_align(["c", "c", "c", "c", "c"])

    temp = flights_list.copy()

    temp.sort(key = lambda flight: flight.destination_city)
    for idx, flight in enumerate(temp):
        if flight.departure_city == vf:
            table.add_row([idx, flight.code, flight.duration, flight.departure_city, flight.destination_city])

    return table



def wind_increase(flights_list, dp_city, minutes):
    for flight in flights_list:
        if flight.departure_city == dp_city:
            flight.duration += minutes

def debugshow(flights_list):
    table = T()
    table.header(["Nr", "Code", "Duration", "Departure City", "Destination City"])
    table.set_cols_align(["c", "c", "c", "c", "c"])

    for idx, flight in enumerate(flights_list):
        table.add_row([idx, flight.code, flight.duration, flight.departure_city, flight.destination_city])

    return table