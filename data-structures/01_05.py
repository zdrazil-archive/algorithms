# Write a method to replace all spaces in a string with '%20'

string = input('Enter string:')


def replace_spaces(input_string):
    string_array = list(input_string)
    print(string_array)
    for ind, val in enumerate(string_array):
        if val == " ":
            string_array[ind] = '%20'
    print(string_array)
    return ''.join(string_array)


print(replace_spaces(string))
