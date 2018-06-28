# This function return a array according to the user gives


def create_array():
    array = []
    length = int(input('Insert the length of the array:'))
    for i in range(length):
        value = input('Insert the value:')
        array.append(value)
    return array


# This function print the array received in the argument

def print_array(array):
    print(array)


print_array(create_array())
