#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum1(arr):
    # Write your code here
    minpos = arr.index(min(arr))
    maxpos = arr.index(max(arr))
    maxsum = sum([i for i in arr if i != arr[minpos]])
    minsum = sum([i for i in arr if i != arr[maxpos]])
    print(minsum, maxsum)


# Efficient Code -
def miniMaxSum2(arr):
    # Write your code here
    sortedarr = sorted(arr)
    minsum = sum(sortedarr[:len(arr) - 1])
    maxsum = sum(sortedarr[1:])
    print(minsum, maxsum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum1(arr)
    miniMaxSum2(arr)
