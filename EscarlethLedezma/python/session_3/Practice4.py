dictionary = {}


# This function create the dictionary according the parameters given for the user
def create_dictionary():
    length = int(input('Enter the dictionary length'))
    global dictionary
    for i in range(length):
        key = input('Enter the dictionary key')
        value = input('Enter the dictionary value')
        dictionary[key] = value
    return dictionary


create_dictionary()


# This function return the list of keys
def print_keys():
    return dictionary.keys()


print("The list of keys are:", print_keys())


# This function return the list of values
def print_values():
    return dictionary.values()


print("The list of values are:", print_values())


# This function return the dictionary
def print_dictionary():
    return dictionary


print("The dictionary is:", print_dictionary())


# This function return if given a key exist in the dictionary
def key_exist_on_dictionary():
    key = input('Insert a key to search')
    return key in dictionary


print("The key exist in the dictionary:", key_exist_on_dictionary())


# This function return if given a value exist in the dictionary
def value_exist_on_dictionary():
    value = input('Insert a value to search')
    return value in dictionary.values()


print("The value exist in the dictionary:", value_exist_on_dictionary())
