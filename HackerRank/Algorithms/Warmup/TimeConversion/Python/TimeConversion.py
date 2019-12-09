#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hours = s[:2]
    minutes = s[3:5]
    seconds = s[6:8]
    suffix = s[8:10]

    if suffix == 'PM':
        hours = str(int(hours) + 12)
        if hours == '24':
            hours = '12'
    else:
        if hours == '12':
            hours = '00'

    return ':'.join([hours, minutes, seconds])

# Challenge definitions
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
