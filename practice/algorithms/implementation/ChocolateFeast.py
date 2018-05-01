#!/bin/python3

import sys
import math

def chocolateFeast(n, c, m):
    # Complete this function
    chocolates = math.floor(n / c)
    wraps = chocolates
    
    while (wraps >= m):
        new_chocolates = math.floor(wraps/m)
        wraps = new_chocolates + (wraps % m)
        chocolates += new_chocolates
    return chocolates

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        result = chocolateFeast(n, c, m)
        print(result)

