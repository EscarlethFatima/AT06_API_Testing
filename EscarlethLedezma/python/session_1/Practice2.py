# This function is to execute arithmetic operations given a operator


def operators(param1, param2, operator):
    if operator == "+":
        print("The sum result is", param1 + param2)
    if operator == "-":
        print("The rest result is", param1 - param2)
    if operator == "*":
        print("The multiply result is", param1 * param2)
    if operator == "/":
        print("The divisor result is", param1 / param2)


operators(1500, 345.5, "+")
operators(2999.5, 58.5, "-")
operators(166, 13, "*")
operators(25799, 9, "/")
