from functions import *
import re

def help_menu():
        print("Available commands:")
        print("  add <code> <name> <type> <species>")
        print("       Add a new animal to the zoo.")
        print("       Example: add 101 Alex herbivore zebra\n")

        print("  modify <code> <new_type>")
        print("       Modify the type of the animal with the given code.")
        print("       Example: modify 101 carnivore\n")

        print("  error <species> <new_type>")
        print("       Change the type of ALL animals belonging to the given species.")
        print("       Example: error lion carnivore\n")

        print("  show <type>")
        print("       Show all animals of the given type sorted by name.")
        print("       Example: show herbivore\n")

        print("  show all")
        print("       List all animals in the zoo.\n")

        print("  help")
        print("       Show this help menu.\n")

        print("  exit")
        print("       Exit the application.")


def menu_start(animal_list):
    print("Welcome to Zoo!")
    add_animal(animal_list, 101, "Simba", "carnivore", "lion")
    add_animal(animal_list, 102, "Nala", "carnivore", "lion")
    add_animal(animal_list, 103, "Marty", "herbivore", "zebra")
    add_animal(animal_list, 104, "Melman", "herbivore", "giraffe")
    add_animal(animal_list, 105, "Gloria", "omnivore", "hippo")
    while True:
        cmd = input("> ")

        if cmd == "exit":
            break

        if cmd == "help":
            help_menu()

        try:
            if cmd.startswith("add"):
                m  = re.match("add (\d+) (\S+) (\S+) (\S+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                code = int(m.group(1))
                name = m.group(2)
                a_type = m.group(3)
                species = m.group(4)

                add_animal(animal_list, code, name, a_type, species)

            elif cmd.startswith("modify"):
                m = re.match("modify (\d+) (\S+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                code = int(m.group(1))
                new_type = m.group(2)

                modify_type(animal_list, code, new_type)

            elif cmd.startswith("error"):
                m = re.match("error (\S+) (\S+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                species = m.group(1)
                new_type = m.group(2)

                error_modify(animal_list, species, new_type)

            elif cmd == "show all":
                print(test_animal_show(animal_list).draw())

            elif cmd.startswith("show"):
                m = re.match("show (\S+)", cmd)
                if not m:
                    raise ValueError("Invalid command")

                a_type = m.group(1)
                print(show_animlas_type(animal_list, a_type).draw())

            else: print("Invalid command")

        except ValueError as e:
            print("Error: ", e)
