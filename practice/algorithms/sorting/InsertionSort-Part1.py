#!/bin/python3

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    element = arr[-1]
    for i in reversed(range(n - 1)):
        if arr[i] > element:
            arr[i + 1] = arr[i]
            print(" ".join(map(str, arr)))
        else:
            arr[i + 1] = element
            print(" ".join(map(str, arr)))
            break
    if element < min(arr):
        arr[0]=element
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

