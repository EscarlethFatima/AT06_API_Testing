# This function return a dictionary with the letters existing and number of occurrences given a word


def convert_string_to_dictionary(string):
    dictionary = {}
    for i in string.lower().replace(" ",""):
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return sorted(dictionary.items())


print(convert_string_to_dictionary("ThiS is String with Upper and lower case Letters"))
print(convert_string_to_dictionary("AAAAA"))
print(convert_string_to_dictionary("There are other ways to cONVERT a dicTIONARY"))