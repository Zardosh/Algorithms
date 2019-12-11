#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    current_height = 0
    number_of_valleys = 0

    for direction in s:
        if direction == 'D':
            # Checks when a new valley starts
            if current_height == 0:
                number_of_valleys += 1
            current_height -= 1
        else:
            current_height += 1

    return number_of_valleys

# Challenge definitions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
