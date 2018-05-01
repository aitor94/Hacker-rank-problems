#!/bin/python3

import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    total = 0
    if not(any(ext in password for ext in numbers)):
        total += 1
    if not(any(ext in password for ext in lower_case)):
        total += 1
    if not(any(ext in password for ext in upper_case)):
        total += 1
    if not(any(ext in password for ext in special_characters)):
        total += 1
    if n + total < 6:
        total += 6 - (n + total)
    return total
        
    

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)

