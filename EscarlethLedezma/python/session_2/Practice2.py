# This function is to determine area of a circle


def area_of_circle(radio):
    pi = 3.1416
    if radio > 10: print("The area is:", pi * radio ** 2)
    else: print("The radio is minor to 10")


area_of_circle(15)
area_of_circle(1000)


# This function is to determine the sum of all integer numbers up to
# and including only until any value lower than 35
# and if is major the sum to 35 will be returned


def sum_to(n):
    sum = 0
    if n > 35: n = 35
    for i in range((n + 1)):
        sum += i
    print(sum)


sum_to(1)
sum_to(10)
sum_to(50)


# This function is to determine the number of days given the name of a month

def days_in_month(month):
    if month is "February":
        return 28
    if month is "April" or month is "June" or month is "September" or month is "November":
        return 30
    if month is "January" or month is "March" or month is "May" or month is "August" or month is "October" or month is "December":
        return 31


print(days_in_month("February"))
print(days_in_month("November"))
print(days_in_month("May"))
print(days_in_month("Hello"))