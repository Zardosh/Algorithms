#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topics):
    teams_with_known_topics_number = []

    for i in range(len(topics) - 1):
        for j in range(i + 1, len(topics)):
            i_known_topics = topics[i]
            j_known_topics = topics[j]
            number_of_known_topics = i_known_topics.count('1')
                
            for char_index in range(len(j_known_topics)):
                if j_known_topics[char_index] == '1' and i_known_topics[char_index] == '0':
                    number_of_known_topics += 1

            teams_with_known_topics_number.append(number_of_known_topics)

    max_topics = max(teams_with_known_topics_number)

    return [max_topics, teams_with_known_topics_number.count(max_topics)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
