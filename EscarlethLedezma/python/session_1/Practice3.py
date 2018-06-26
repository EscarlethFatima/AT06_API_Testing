# This function is to execute sum or rest operation using(comparison,assignment,logic,identity operators)


def operation_sum_or_rest(number1, number2, operator):
    print("-----------------OPERATION SUM OR REST-----------------")
    if id(operator) == id("sum") or operator is "rest":
        if number1 >= number2 and number1 <= 100:
            number1 += number2
            print("***** number1 is major to number2 and minor to 100 *****")
            print("The sum result is:", number1)
        else:
            number2 -= number1
            print("***** number1 is not major to number2 or is major to 100 *****")
            print("The rest result is:", number2)
    else:
        print("Is not a sum or res operation")


operation_sum_or_rest(10, 5, "sum")
operation_sum_or_rest(5, 100, "rest")
operation_sum_or_rest(0, 0, "division")


# This function is to execute multiply or division operation using(comparison,assignment,logic,identity operators)

def operation_multiply_or_division(number1, number2, operator):
    print("-----------------OPERATION MULTIPLY OR DIVISION-----------------")
    if operator == "multiply" or operator is "division":
        if number1 != number2:
            number2 *= number2
            print("***** number1 is not equal to number2 *****")
            print("The multiply result is:", number2)
        else:
            number1 /= number2
            print("***** number1 is equal to number2 *****")
            print("The division result is:", number1)
    else:
        print("Is not a multiply or division operation")


operation_multiply_or_division(10, 5, "multiply")
operation_multiply_or_division(5000, 5000, "division")
operation_multiply_or_division(10, 5, "hello")


# This function is to execute modulus operation using(comparison,assignment,logic,identity,membership operators)

def operation_exist_or_not_exist_in_list(value1, value2, list):
    print("-----------------OPERATION EXIST OR NOT EXIST IN LIST-----------------")
    if value1 in list:
        print("***** value1 exist in list *****")
        if type(value1) is int and value1 > 0:
            value1 %= value2
            print("***** value1 is type of int and is major to 0 *****")
            print("The modulus result is:", value1)
        else:
            print("value1 is not type of int or is minor to 1")
    elif value2 not in list:
        print("***** value2 doesn't exist in list *****")
        if type(value2) is float and value2 < 1000:
            value2 %= value1
            print("***** value2 is type of float and is minor to 1000 *****")
            print("The modulus result is:", value2)
        else:
            print("value1 is not type of float or is minor to 1")


operation_exist_or_not_exist_in_list(10, 100, [10, 20, 30, 40, 50, 60])
operation_exist_or_not_exist_in_list(-10, 100, [-10, 20, 30, 40, 50, 60])
operation_exist_or_not_exist_in_list(510.0, 100, [10, 20, 30, 40, 50, 60, 510.0])
operation_exist_or_not_exist_in_list(11, 100.0, [1, 2, 3, 4, 5, 6])
operation_exist_or_not_exist_in_list(11, 100, [1, 2, 3, 4, 5, 6])
operation_exist_or_not_exist_in_list(11, 2000, [1, 2, 3, 4, 5, 6])
