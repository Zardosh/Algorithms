#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    broken_records = [0, 0]

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            broken_records[0] += 1
        elif score < min_score:
            min_score = score
            broken_records[1] += 1
    
    return broken_records

# Challenge definitions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
