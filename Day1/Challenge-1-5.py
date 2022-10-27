#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(count, array):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for i in array:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        elif i == 0:
            zero += 1
    print(Decimal(round(pos / count, 6)).quantize(Decimal('0.000000')))
    print(Decimal(round(neg / count, 6)).quantize(Decimal('0.000000')))
    print(Decimal(round(zero / count, 6)).quantize(Decimal('0.000000')))


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(n, arr)
