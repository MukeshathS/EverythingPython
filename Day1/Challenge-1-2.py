#!/bin/python3

import math
import os
import random
import re
import sys
from pprint import pprint


def weird_or_not_weird(number):
    if not (number % 2 == 0):
        return "Weird"
    elif number % 2 == 0:
        if (number >= 2) and (number <= 5):
            return "Not Weird"
        elif (number >= 6) and (number <= 20):
            return "Weird"
        elif number > 20:
            return "Not Weird"
        else:
            return "Internal Error"
    else:
        return "Internal Error"


if __name__ == '__main__':
    n = int(input().strip())
    weirdText = weird_or_not_weird(n)
    print(weirdText)

