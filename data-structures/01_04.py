# Write a method to decide if two string are anagrams or not

string1 = 'William Shakespeare'
string2 = 'I am a weakish speller'


def is_anagram(string1, string2):
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    string1 = string1.lower()
    string2 = string2.lower()

    string1 = sorted(string1)
    string2 = sorted(string2)

    if string1 == string2:
        return True
    else:
        return False


print(is_anagram(string1, string2))
