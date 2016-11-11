# Assume you have a method isSubstring which checks if one word is a
# substring of another. Given two strings, s1 and s2, write code to check
# if s2 is a rotation of s1 using only one call to isSubstring (i.e.
# "watterbottle" is a rotation of "terbottlewat)

string1 = 'watterbottle'
string2 = 'erbottlewat'


def is_substring(s1, s2):
    return


def is_rotation(s1, s2):
    return len(s1) == len(s2) and is_substring(s1 + s1, s2)
