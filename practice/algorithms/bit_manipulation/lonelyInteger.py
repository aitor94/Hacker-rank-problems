#!/bin/python3

import sys
from collections import Counter

def lonelyinteger(a):
    # Complete this function
    counts = Counter(a)
    for element, count in counts.items():
        if count == 1:
            return element

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
