from functions import *
import re

def help_menu():
    print("Available commands:")
    print("")
    print("  add <name> <month> <cost> <artists>")
    print("       Add a new festival.")
    print("       Month must be between 1 and 12.")
    print("       Festival names must be unique.")
    print("       Example: add Untold 8 350 TheChainsmokers")
    print("")
    print("  show all")
    print("       Show all festivals.")
    print("")
    print("  show <season>")
    print("       Show festivals from a season (winter, spring, summer, autumn).")
    print("       Example: show summer")
    print("")
    print("  show <artist>")
    print("       Show all festivals where the given artist performs.")
    print("       Sorted by month.")
    print("       Example: show Armin")
    print("")
    print("  help")
    print("       Display this help menu.")
    print("")
    print("  exit")
    print("       Exit the application.")

def start_menu(festivals):
    print("=====MUSIC FESTIVAL=====")
    add_festival(festivals, "Antold", 8, 350, "Armin VanBuuren, Kygo, Lost Frequencies")
    add_festival(festivals, "ElectricCastle", 7, 280, "Skrillex, Twenty One Pilots, Netsky")
    add_festival(festivals, "Neversea", 7, 300, "Clean Bandit, Steve Aoki, Alan Walker")
    add_festival(festivals, "Tomorrowland", 6, 500, "David Guetta, Martin Garrix, Tiesto")
    add_festival(festivals, "Coachella", 4, 450, "Bad Bunny, Billie Eilish, The Weeknd")
    add_festival(festivals, "RockWerchter", 7, 320, "Imagine Dragons, Arctic Monkeys, Metallica")

    while True:
        cmd = input("> ")

        if cmd =="exit":
            break

        if cmd =="help":
            help_menu()

        try:
            if cmd.startswith("add"):
                m = re.match("add (\S+) (\d+) (\d+) (.+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                name = m.group(1)
                month = int(m.group(2))
                cost = int(m.group(3))
                artits = m.group(4)

                add_festival(festivals, name, month, cost, artits)

            elif cmd == "show all":
                print(show_all(festivals).draw())

            elif cmd.startswith("show"):
                if "winter" in cmd or "summer" in cmd or "autumn" in cmd:
                    m = re.match("show (\S+)", cmd)
                    if not m:
                        raise ValueError("Invalid command")

                    season = m.group(1)
                    print(show_season(festivals, season).draw())

                else:
                    m = re.match("show (.+)", cmd)
                    if not m:
                        raise ValueError("Invalid command")

                    artist = m.group(1)
                    print(show_artist(festivals, artist).draw())

            else:
                print("Invalid command")

        except ValueError as e:
            print("Error: ", e)
