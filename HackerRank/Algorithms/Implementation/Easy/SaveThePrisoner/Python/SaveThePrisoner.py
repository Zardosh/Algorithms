#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    pass_from_chair = m % n - 1

    if pass_from_chair + s > n:
        return pass_from_chair - (n - s)
    elif pass_from_chair + s < 1:
        return n
    else:
        return pass_from_chair + s

# Challenge definitions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
