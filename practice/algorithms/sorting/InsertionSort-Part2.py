#!/bin/python3

import sys

def insertionSort2(n, arr):
    # Complete this function
    for i in range(1,len(arr)):
        j = i - 1
        key = arr[i]
        while(j >=0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(" ".join(map(str, arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
