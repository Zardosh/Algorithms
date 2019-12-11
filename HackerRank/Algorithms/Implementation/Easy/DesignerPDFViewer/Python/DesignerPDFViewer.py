#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    all_letters_with_height = {'abcdefghijklmnopqrstuvwxyz'[i]: h[i] for i in range(0,26)} 

    return max([all_letters_with_height[letter] for letter in word]) * len(word)

# Challenge definitions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
