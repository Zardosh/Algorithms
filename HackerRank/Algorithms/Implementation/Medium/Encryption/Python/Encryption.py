#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    number_of_columns = math.ceil(math.sqrt(len(s)))
    final_string = ""

    for column_index in range(number_of_columns):
        for i in range(column_index, len(s), number_of_columns):
            final_string += s[i]
        final_string += " "

    return final_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
