# Implement an algorithm to determine if a string has all unique
# characters. What if you can not use additional data structures?

string = 'Lorem ipsum'


def check_unique(input_string):
    char_set = [0 for x in range(256)]
    for ind, val in enumerate(input_string):
        string_value = ord(val)
        char_set[string_value] += 1
        if char_set[string_value] > 1:
            return False
    return True


result = check_unique(string)
print(result)
