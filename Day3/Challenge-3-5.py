#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1 = 0
    d2 = 0
    n = len(arr[0])

    for i in range(n):
        d1 = d1 + arr[i][i]
        d2 = d2 + arr[i][n - i - 1]

    # Or

    d1 = 0
    d2 = 0
    n = len(arr[0])
    for i in range(n):
        for j in range(n):
            if i == j:
                d1 += arr[i][j]
            if i == n - j - 1:
                d2 += arr[i][j]

    return abs(d1 - d2)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)