#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    total_likes = 2
    day_likes = 2

    if n > 1:
        for day in range(2, n + 1):
            total_likes += day_likes * 3 // 2
            day_likes = day_likes * 3 // 2

    return total_likes

# Challenge definitions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
