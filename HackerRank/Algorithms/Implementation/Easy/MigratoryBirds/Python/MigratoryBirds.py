#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird_counts_per_type = [arr.count(i) for i in range(1, 6)]

    # Sums 1 to index to get the corresponding bird type
    return bird_counts_per_type.index(max(bird_counts_per_type)) + 1

# Challenge definitions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
