#!/bin/python3

import math
import os

# Complete the findMedian function below.
def findMedian(arr):
    median_index = math.floor(len(arr) / 2)
    return sorted(arr)[median_index]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

