from texttable import Texttable

def create_animal(code, name, a_type, species):
    return {
        'code': code,
        'name': name,
        'type': a_type,
        'species': species
    }

def get_code(a):
    return a['code']
def get_name(a):
    return a['name']
def get_type(a):
    return a['type']
def get_species(a):
    return a['species']

def set_code(a , n):
    a['code'] = n
def set_name(a, n):
    a['name'] = n
def set_type(a, n):
    a['type'] = n
def set_species(a, n):
    a['species'] = n

def validate_input(code, name, a_type, species):
    if code is None or str(code).strip() == "":
        raise ValueError("Code is required")

    if name.strip() == "":
        raise ValueError("Name is required")

    if a_type.strip() == "":
        raise ValueError("Type is required")

    if species.strip() == "":
        raise ValueError("Species is required")

def add_animal(animal_list, code, name, a_type, species):
    validate_input(code, name, a_type, species)

    for animal in animal_list:
        if get_code(animal) == code:
            raise ValueError("Animal Already Exists")

    animal_list.append(create_animal(code, name, a_type, species))


def modify_type(animal_list, code, new_type):
    for animal in animal_list:
        if get_code(animal) == code:
            set_type(animal, new_type)

def error_modify(animal_list, species, new_type):
    if new_type.strip() == "":
        raise ValueError("Type is required")

    for animal in animal_list:
        if get_species(animal) == species:
            set_type(animal, new_type)

def show_animlas_type(animal_list, animal_type):
    a_copy = animal_list.copy()
    a_copy.sort(key = lambda a_copy: get_name(a_copy))

    table = Texttable()
    table.header(["Animal Code", "Animal Name", "Animal Type", "Species"])
    table.set_cols_align(["c", "c", "c", "c"])

    for animal in a_copy:
        if get_type(animal) == animal_type:
            table.add_row([get_code(animal), get_name(animal), get_type(animal), get_species(animal)])


    return table


def test_animal_show(animal_list):
    table = Texttable()
    table.header(["Animal Code", "Animal Name", "Animal Type", "Species"])
    table.set_cols_align(["c", "c", "c", "c"])

    for animal in animal_list:
        table.add_row([get_code(animal), get_name(animal), get_type(animal), get_species(animal)])

    return table