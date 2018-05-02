#!/bin/python3

import sys

numbers = [
        "zero", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"
]

def timeInWords(h, m):
    # Complete this function
    if m == 0:
        return numbers[h] + " o' clock"
    if m == 30:
        return "half past " + numbers[h]
    if m == 15:
        return "quarter past " + numbers[h]
    if m == 45:
        return "quarter to " + numbers[h + 1]
    if m == 1:
        return "one minute past " + numbers[h]
    if m == 59:
        return "one minute to " + numbers[h + 1]
    if m < 30:
        return numbers[m] + " minutes past " + numbers[h]
    if m < 59:
        return numbers[60 - m] + " minutes to " + numbers[h + 1]
    
        

if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)

