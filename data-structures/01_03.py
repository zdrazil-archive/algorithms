# Design an algorithm and write code to remove duplicate characters in a
# string without using any additional buffer. NOTE: one or two variables
# are fine. An extra copy of an array is not.

string = 'abfcdfe2'


def remove_dup(input_string):
    string_array = list(input_string)
    for ind, val in enumerate(string_array):
        for j_ind, j_val in enumerate(string_array):
            if (ind != j_ind) and (val == j_val) and j_val != '':
                string_array[j_ind] = ''

    return ''.join(string_array)


print(string)
print(remove_dup(string))
