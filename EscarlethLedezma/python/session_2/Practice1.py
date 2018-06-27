# This function is to determine if a number is odd or even


def odd_or_even(number):
    if number % 2 == 0: print("This number is even")
    else: print("This number is odd")


odd_or_even(2)
odd_or_even(15)
odd_or_even(444.0)


# This function is to determine all prime numbers given a min and max range
# (all is to determine if all elements of the iterable are true)

def prime(min, max):
    for x in range(min, max + 1):
        if all (x % y != 0 for y in range(2, x)):
            print(x)


prime(20, 30)
prime(100, 150)
prime(15, 25)
