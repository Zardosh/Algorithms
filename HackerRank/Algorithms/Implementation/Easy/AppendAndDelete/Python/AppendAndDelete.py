#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    moves = 0

    while not t.startswith(s):
        s = s[:-1]
        moves += 1

    if s == '':
        return 'Yes' if k - moves >= len(t) else 'No'

    while not t == s:
        s += t[len(s)]
        moves += 1

    if (moves <= k and (k - moves) % 2 == 0) or (k - moves >= 2 * len(s) + 1):
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
