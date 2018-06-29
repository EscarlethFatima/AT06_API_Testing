import CalculateAge as convert_age
import PrintAge as print_age

users_age = {}


# This function saves the users with age

def save_users():
    global users_age
    cant_users = int(input('Enter the users quantity:'))
    for i in range(cant_users):
        name = input('Enter the user name:')
        age = int(input('Enter the user age:'))
        users_age[name] = age


# This function return age according to conditionals

def expected_message_age(age):
    if age <= 12:
        return print_age.print_age_child()
    if 12 < age < 18:
        return print_age.print_age_teenager()
    if 18 <= age < 30:
        return print_age.print_age_young()
    if age >= 30:
        return print_age.print_age_adult()


# This function prints the age converted to days,hours,minutes,and the expected message age

def print_users_with_ages():
    for i in users_age:
        print(i, ' AGE')
        print('The age in days is:', convert_age.calculate_age_days(users_age[i]))
        print('The age in hours is:', convert_age.calculate_age_hours(users_age[i]))
        print('The age in minutes is:', convert_age.calculate_age_minutes(users_age[i]))
        print(expected_message_age(users_age[i]))


save_users()
print_users_with_ages()
