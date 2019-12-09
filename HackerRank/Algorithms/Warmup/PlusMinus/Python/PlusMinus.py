#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_numbers_ratio = round(len([number for number in arr if number > 0]) / len(arr), 6)
    negative_numbers_ratio = round(len([number for number in arr if number < 0]) / len(arr), 6)
    zero_ratio = round(len([number for number in arr if number == 0]) / len(arr), 6)

    print(positive_numbers_ratio, negative_numbers_ratio, zero_ratio, sep="\n")

# Challenge definitions
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
