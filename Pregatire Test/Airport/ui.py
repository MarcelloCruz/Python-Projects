import re
from functions import *

def menu_start():
    print("Welcome to Airport App")
    print("Type help to see the commands")

def menu_ui(flights):
    menu_start()
    add_flight(flights, "OB301", 45, "Cluj", "London")
    add_flight(flights, "AB221", 60, "Cluj", "Madrid")
    add_flight(flights, "XR900", 85, "Timisoara", "Paris")
    add_flight(flights, "TT111", 30, "Iasi", "Berlin")
    add_flight(flights, "MK550", 120, "Cluj", "Rome")
    add_flight(flights, "ZZ777", 50, "Oradea", "Vienna")
    add_flight(flights, "HG420", 75, "Sibiu", "Amsterdam")
    add_flight(flights, "DR333", 25, "Cluj", "Prague")
    add_flight(flights, "LN888", 95, "Arad", "Oslo")
    add_flight(flights, "QR123", 40, "Craiova", "Brussels")

    while True:
        cmd = input("> ").strip()

        if cmd == "exit":
            break

        if cmd == "help":
            print("Available commands:")
            print("  add <code> <duration> <departure_city> <destination_city>")
            print("  show all")
            print("  show <departure_city>")
            print("  delete <code>")
            print("  increase <departure_city> with <minutes>")
            print("  help")
            print("  exit")
            continue

        try:
            # ADD
            if cmd.startswith("add"):
                m = re.match(r"add (\S+) (\d+) (\S+) (\S+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                code = m.group(1)
                dr = int(m.group(2))
                dpc = m.group(3)
                dsc = m.group(4)

                if len(code) < 3 or len(dpc) < 3 or len(dsc) < 3 or dr < 20:
                    raise ValueError("Invalid input")

                add_flight(flights, code, dr, dpc, dsc)

            # SHOW ALL
            elif cmd == "show all":
                print(debugshow(flights).draw())

            # SHOW by departure city
            elif cmd.startswith("show"):
                m = re.match(r"show (\S+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                departure = m.group(1)

                print(show_flights(flights, departure).draw())

            # DELETE
            elif cmd.startswith("delete"):
                m = re.match(r"delete (\S+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                code = m.group(1)

                delete_flight(flights, code)

            # INCREASE
            elif cmd.startswith("increase"):
                m = re.match(r"increase (\S+) with (\d+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                departure = m.group(1)
                minutes = int(m.group(2))

                if not 10 <= minutes <= 60:
                    raise ValueError("Minutes out of range")

                wind_increase(flights, departure, minutes)

            else:
                print("Invalid command")

        except ValueError as e:
            print("Error:", e)
