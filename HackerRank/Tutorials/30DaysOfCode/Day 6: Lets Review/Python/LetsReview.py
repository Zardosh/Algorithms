# Enter your code here. Read input from STDIN. Print output to STDOUT
import os

def even_and_odd_string_characters(string):
    even_characters = ""
    odd_characters = ""

    for i in range(len(string)):
        if i % 2 == 0:
            even_characters += string[i]
        else:
            odd_characters += string[i]

    return "{} {}".format(even_characters, odd_characters)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        string = str(input())

        result = even_and_odd_string_characters(string)

        fptr.write(result + '\n')

    fptr.close()
