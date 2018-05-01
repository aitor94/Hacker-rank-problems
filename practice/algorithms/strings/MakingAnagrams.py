#!/bin/python3

import sys

def makingAnagrams(s1, s2):
    # Complete this function
    letters = "abcdefghijklmnopqrstuvwxyz"
    difference = 0
    for letter in letters:
        c1 = s1.count(letter)
        c2 = s2.count(letter)
        difference += abs(c1 - c2)
    return difference
        
s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)

