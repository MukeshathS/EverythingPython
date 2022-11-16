# Replace a character at a position in a string and print new string

def mutate_string(string, position, character):
    text = list(string)
    text[position] = character
    return ''.join(text)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

###################################################################
# Count number of substring in main string

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - (len(sub_string) - 1)):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
        else:
            continue
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

########################################################################

# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Output Format
#
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.


if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for t in s:
        if t.isalnum() and alnum == False:
            alnum = True
        if t.isalpha() and alpha == False:
            alpha = True
        if t.isdigit() and digit == False:
            digit = True
        if t.islower() and lower == False:
            lower = True
        if t.isupper() and upper == False:
            upper = True

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)


###################################################################################################

# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    return " ".join([i.capitalize() for i in s.split(" ")])


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
