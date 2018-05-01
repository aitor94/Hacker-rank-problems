#!/bin/python3

import sys

def icecreamParlor(m, arr):
    # Complete this function
    idx1 = 0
    for index, price in enumerate(arr):
        rest = m - price
        if rest in arr[index+1:]:
            idx1 = index
            break
    idx2 = arr[idx1+1:].index(rest) + 2 + idx1
    return sorted([idx1 + 1, idx2])
        

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print (" ".join(map(str, result)))

