dictionary = {}


# This function return the key inserted by the user

def get_the_key():
    while True:
        key = int(input('Insert the key(should be values[1-9]):'))
        if 0 < key < 10:
            return key
        else:
            print("ERROR:Insert a valid number in range[1-9]")
            pass


# This function return a dictionary where keys are defined by the user in a range[1-9]
# and the values are squares of these

def dictionary_in_range():
    global dictionary
    length = int(input('Insert the dictionary length:'))
    for i in range(length):
        key = get_the_key()
        dictionary[key] = key ** 2
    return dictionary


print("The dictionary is:", dictionary_in_range())


# This function return true if the number is prime
def is_prime(number):
    if number is 1 or number is 0:
        return False
    return all(number % y != 0 for y in range(2, number))


# This function return a dictionary that contains all prime numbers


def dictionary_with_prime_numbers():
    prime_dictionary = {}
    for i in list(dictionary.keys()):
        if is_prime(i):
            prime_dictionary[i] = dictionary[i]
    return prime_dictionary


print("The dictionary with numbers prime is:", dictionary_with_prime_numbers())
