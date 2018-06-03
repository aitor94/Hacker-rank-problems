#!/bin/python3

import os

#
# Complete the restaurant function below.
#
def restaurant(l, b):
    #
    # Write your code here.
    #
    gcd = 1
    for i in range(1, min([l, b]) + 1):
        if l % i == 0 and b % i == 0:
            gcd = i
    return int((l * b) / (gcd * gcd))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
