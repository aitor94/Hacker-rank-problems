#!/bin/python3

import os

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr = sorted(arr)
    min_diff = abs(arr[1] - arr[0])
    diffs = []
    sol = []
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i - 1])
        diffs.append(diff)
        if diff < min_diff:
            min_diff = diff
    for i in range(len(diffs)):
        if diffs[i] == min_diff:
            sol.append(arr[i])
            sol.append(arr[i + 1])
    return sol

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
