#!/bin/python3

import os

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    common_length = 0
    for chr in range(min(len(s), len(t))):
        if s[chr] == t[chr]:
            common_length+=1
        else:
            break
    
    if len(s) + len(t) - 2 * common_length > k:
        return "No"
    elif (len(s) + len(t) - 2 * common_length) % 2 == k % 2:
        return "Yes"
    elif len(s) + len(t) - k < 0:
        return "Yes"
    else:
        return "No"

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

