#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_score = int(a[0] > b[0]) + int(a[1] > b[1]) + int(a[2] > b[2])
    b_score = int(b[0] > a[0]) + int(b[1] > a[1]) + int(b[2] > a[2])
    return [a_score, b_score]

# Challenge definitions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
