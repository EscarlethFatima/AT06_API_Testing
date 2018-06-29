import re

dictionary_users = {}


# This function is to return the user_id if a user id is in range[1-100]


def verify_user_id():
    while True:
        user_id = int(input('Insert the user id in range(1-100):'))
        if 0 < user_id <= 100:
            return user_id
        else:
            print('ERROR: Enter a user id in range(1-100)')


# This function is to return the user_name if a user name contains letters in lowercase

def verify_user_name():
    while True:
        user_name = input('Insert the user name only letters lowercase:')
        if re.match("[a-z]{1,8}$", user_name):
            return user_name
        else:
            print('ERROR: Enter a user id in range(1-100)')


# This function is to save the user id and the user name inside of a dictionary

def save_users_with_id():
    global dictionary_users
    length = int(input('Please,Insert the users quantity:'))
    for i in range(length):
        key = verify_user_id()
        dictionary_users[key] = verify_user_name()


save_users_with_id()


# This function is to return a list that contains the keys that start with number given.

def start_user_id():
    array = []
    number = input('Please insert the number to search in the userid:')
    for key in dictionary_users:
        if key.startswith(number):
            array.append(key)
    return array


print('The user id list with the similarities is:', start_user_id())


# This function is to return a list that contains the value that start with letter given.

def start_user_name():
    array = []
    letter = input('Please insert the letter to search in the username:')
    for key in dictionary_users:
        if dictionary_users[key].startswith(letter):
            array.append(key)
    return array


print('The user name list with the similarities is:', start_user_name())


# This function is to print all the users and which group belong.

def print_search_in_group():
    for key in dictionary_users:
        if 1 <= key < 26:
            return f"User {dictionary_users[key]} belongs to Group 1"
        if 26 <= key < 51:
            return f"User {dictionary_users[key]} belongs to Group 2"
        if 51 <= key < 76:
            return f"User {dictionary_users[key]} belongs to Group 3"
        if 76 <= key <= 100:
            return f"User {dictionary_users[key]} belongs to Group 4"


print("*************Groups to which the users belong*************")
print(print_search_in_group())
