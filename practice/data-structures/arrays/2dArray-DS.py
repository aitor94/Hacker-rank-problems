#!/bin/python3

import os
import sys

#
# Complete the array2D function below.
#
def array2D(arr):
    #
    # Write your code here.
    #
    summ = 0
    first = True
    for row in range(len(arr) - 2):
        for col in range(len(arr[row]) - 2):
            actual = 0
            actual += arr[row][col]
            actual += arr[row][col + 1]
            actual += arr[row][col + 2]
            actual += arr[row + 1][col + 1]
            actual += arr[row + 2][col]
            actual += arr[row + 2][col + 1]
            actual += arr[row + 2][col + 2]
            if first:
                first = False
                summ = actual
                continue
            if actual > summ:
                summ = actual
    return summ
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = array2D(arr)

    fptr.write(str(result) + '\n')


