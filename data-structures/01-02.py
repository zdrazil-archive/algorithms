# Write code to reverse a C-Style String (C-String means that "abcd" is represented as five characters, including null character)

string = 'abcd\n'

def reverse_string(input):
    reverse_string_array = []

    input = input[:-1]

    for ind, val in enumerate(input):
        reverse_string_array.append(input[len(input) - ind - 1])
    
    return ''.join(reverse_string_array) + '\n'

print(string)
print(reverse_string(string))
