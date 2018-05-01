#!/bin/python3

import sys

def alternatingCharacters(s):
    # Complete this function
    first = s[0]
    total = 0
    for letter in s[1:]:
        if letter == first:
            total += 1
        first = letter
    return total

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
