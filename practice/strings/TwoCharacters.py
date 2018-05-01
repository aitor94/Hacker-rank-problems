#!/bin/python3

import sys
import itertools
import re

def isConsecutive(s):
    if len(list(set(s))) != 2:
        return False
    else:
        last_letter = s[0]
        for letter in s[1:]:
            if letter==last_letter:
                return False
            else:
                last_letter = letter
        return True

def twoCharaters(s):
    # Complete this function
    distinct_letters = list(set(s))
    pairs = []
    for i, j in itertools.product(distinct_letters, distinct_letters):
        pair = ''.join(sorted(i + j))
        if i != j:
            pairs.append(pair)
    pairs = list(set(pairs))
    result = 0
    lengths = [0]
    for pair in pairs:
        new_str = re.sub('[^'+pair+']', '', s)
        if isConsecutive(new_str):
            lengths.append(len(new_str))
    m = max(lengths)
    return m

if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    print(result)

