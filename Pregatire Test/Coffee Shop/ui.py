from functions import *
import re

def help_menu():
    print("""
Available commands:

 add <name> <country> <price>
     Add a new coffee.
     - Price must be a positive float.
     Example: add Lavazza Italy 5.5

 show
     Display all coffees sorted alphabetically by country,
     and if countries are equal, sorted increasingly by price.

 filter <country> <price>
     Show all coffees from <country> with price ≤ <price>.
     Example: filter Brazil 10

 filter <country>
     Only filter by country (any price accepted).
     Example: filter Ethiopia

 filter <price>
     Only filter by price (all coffees with price ≤ value).
     Example: filter 7.5

 If NO coffees match, the message "No such coffees" will be displayed.

 help
     Show this help menu.

 exit
     Exit the application.
""")


def menu_start(shops):
    print("=====COFFEE SHOP=====")
    add_coffe(shops, "CaffeMiel", "France", 5.5)
    add_coffe(shops, "EspressoRoma", "Italy", 4.2)
    add_coffe(shops, "ColombianGold", "Colombia", 6.0)
    add_coffe(shops, "KonaBlend", "USA", 7.8)
    add_coffe(shops, "EthiopianSunrise", "Ethiopia", 6.7)
    while True:
        cmd = input("> ")

        if cmd == "exit":
            break

        if cmd == "help":
            help_menu()

        try:
            if cmd.startswith("add"):
                m = re.match("add (.+) (.+) ([0-9]*\.?[0-9]+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                name = m.group(1)
                country = m.group(2)
                price = float(m.group(3))

                add_coffe(shops,name, country, price)

            elif cmd == "show all":
                print(show(shops).draw())

            elif cmd.startswith("filter"):
                parts = cmd.split()
                args =parts[1:]

                country = None
                price = None

                if len(args) == 2:
                    country = args[0]
                    price = float(args[1])

                elif len(args) == 1:
                    if args[0].isdigit():
                        price = float(args[0])
                    else:
                        country = args[0]

                elif len(args) == 0:
                    pass

                else:
                    raise ValueError("Invalid command")

                table, found = filter_coffe(shops, country, price)

                if found:
                    print(table.draw())
                else: print("No such coffees")

            else:
                print("Invalid command")

        except ValueError as e:
            print("Error:", e)