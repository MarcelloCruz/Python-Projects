from numpy.distutils.system_info import show_all

from functions import *
import re

def help_menu():
    print("Available commands:")
    print("")
    print("  add <manufacturer> <model> <price>")
    print("       Add a new phone. Fields must each have length ≥ 3.")
    print("       Example: add Samsung GalaxyS24 3200")
    print("")
    print("  show all")
    print("       Show all phones currently in the store.")
    print("")
    print("  find <manufacturer>")
    print("       Show all phones whose manufacturer contains the given string.")
    print("       Partial matches allowed: 'sung' matches 'Samsung'.")
    print("       Example: find sung")
    print("")
    print("  increase <manufacturer> <model> <amount>")
    print("       Increase the price of one phone by a given amount.")
    print("       Example: increase Samsung GalaxyS24 200")
    print("")
    print("  p <percentage>")
    print("       Increase the price of ALL phones by a given percent.")
    print("       Percentage must be between -50 and 100.")
    print("       Example: p 10")
    print("")
    print("  help")
    print("       Show this help menu.")
    print("")
    print("  exit")
    print("       Exit the application.")

def start_menu(phones):
    print("======PHONE STORE======")
    add_phone(phones, "Samsung", "GalaxyS24", 4200)
    add_phone(phones, "Apple", "iPhone15", 5300)
    add_phone(phones, "Xiaomi", "RedmiNote13", 1500)
    add_phone(phones, "Huawei", "P50Pro", 3800)
    add_phone(phones, "Nokia", "XR20", 2100)

    while True:
        cmd = input("> ")
        if cmd == "exit":
            break

        elif cmd == "help":
            help_menu()

        try:
            if cmd.startswith("add"):
                m = re.match("add (\S+) (\S+) (\d+)", cmd)
                if not m:
                    raise  ValueError("Invalid Input")

                manuf = m.group(1)
                model = m.group(2)
                price = int(m.group(3))

                add_phone(phones,manuf,model,price)

            elif cmd == "show all":
                print(shw_all(phones).draw())

            elif cmd.startswith("find"):
                m = re.match("find (\S+)", cmd)
                if not m:
                    raise ValueError("Invalid Input")

                manuf = m.group(1)
                print(find_phone(phones,manuf).draw())

            elif cmd.startswith("increase"):
                m = re.match("increase (\S+) (\S+) (\d+)", cmd)
                if not m:
                    raise ValueError("Invalid Input")

                manuf = m.group(1)
                model = m.group(2)
                add_price = int(m.group(3))

                increase_price(phones,manuf,model,add_price)

            elif cmd.startswith("p"):
                m = re.match("p ([+-]?\d+)", cmd)
                if not m:
                    raise ValueError("Invalid Input")

                percentage = int(m.group(1))
                increase_percentage(phones, percentage)

            else: print("Invalid Command")

        except ValueError as e:
            print("Error: ", e)


