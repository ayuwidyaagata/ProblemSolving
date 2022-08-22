#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus, minus, zero = 0, 0, 0
    m = len(arr)
    for i in range(m):
        if arr[i] > 0:
            plus = plus + 1
        elif arr[i] < 0:
            minus = minus + 1
        else:
            zero = zero + 1
    print(plus/m)
    print(minus/m)
    print(zero/m)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = plusMinus(arr)
