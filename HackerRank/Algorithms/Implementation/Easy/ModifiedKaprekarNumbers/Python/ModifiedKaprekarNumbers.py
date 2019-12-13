#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    output_string = ""

    for number in range(p, q + 1):
        number_length = len(str(number))
        last_part = int(str(number ** 2)[-number_length:])
        first_part_string = str(number ** 2)[:-number_length]
        first_part = 0

        if first_part_string:
            first_part = int(first_part_string)

        if first_part + last_part == number:
            output_string += str(number) + ' '

    print(output_string if output_string else 'INVALID RANGE')
        
        
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
