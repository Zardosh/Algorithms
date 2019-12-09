#!/bin/python3

import math
import os
import random
import re
import sys

def check_weird_number(number):
    if number % 2 != 0 or (number >= 6 and number <= 20):
        print("Weird")
    else:
        print("Not Weird")

# Challenge definitions
if __name__ == '__main__':
    N = int(input())
    check_weird_number(N)
