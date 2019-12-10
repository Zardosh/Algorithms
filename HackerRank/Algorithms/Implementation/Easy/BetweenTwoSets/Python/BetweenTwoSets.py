#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def is_number_factor_of_all_array_elements(factor_number, array):
    for number in array:
        if number % factor_number != 0:
            return False

    return True

def is_number_least_common_multiple(possible_number, array):
    for number in array:
        if possible_number % number != 0:
            return False
    
    return True

def get_least_common_multiple_of_array(array):
    least_common_multiple = max(array)

    while not is_number_least_common_multiple(least_common_multiple, array):
        least_common_multiple += max(array)
    
    return least_common_multiple


def getTotalX(a, b):
    # Write your code here
    if max(a) > min(b):
        return 0
    else:
        a_least_common_multiple = get_least_common_multiple_of_array(a)
        valid_numbers_count = 0

        for possible_number in range(a_least_common_multiple, min(b) + 1, a_least_common_multiple):
            if is_number_factor_of_all_array_elements(possible_number, b):
                valid_numbers_count += 1

        return valid_numbers_count
        
# Challenge definitions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
