#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # x1 + v1 * t = x2 + v2 * t
    # if v1 = v2 and x1 = x2, they will always stay together
    # if v1 = v2 and x1 != x2, they will never meet
    # if t < 0, that means they would need to go backwards to meet
    # if t = 0, that means they are already at the same place
    # if t is not an integer (t % 1 != 0), that means they meet in between jumps and not
    # in a number of the line
    if v1 != v2:
        number_of_jumps_to_meet = (x2 - x1) / (v1 - v2)

        if number_of_jumps_to_meet < 0 or number_of_jumps_to_meet % 1 != 0:
            return "NO"
        else:
            return "YES"
    else:
        return "NO"

# Challenge definitions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
