#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    if s[-2] == "A" and int(s[:2]) == 12:
        h = '00' + s[2:-2]
        return h
    elif s[-2] == "P" and int(s[:2]) == 12:
        h = str(int(s[:2]) + 0) + s[2:-2]
        return h
    elif s[-2] == "P":
        h = str(int(s[:2]) + 12) + s[2:-2]
        return h
    return s[:-2]


def timeConversion1(s):
    # Write your code here
    mil_time_in = datetime.strptime(s, "%I:%M:%S%p")
    mil_time = datetime.strftime(mil_time_in, "%H:%M:%S")
    return mil_time


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    result = timeConversion1(s)
    print(result)
