#!/bin/python3

import sys

def marcsCakewalk(calories):
    # Complete this function
    miles = 0
    for index, calorie in enumerate(sorted(calories, reverse=True)):
        miles += pow(2, index) * calorie
    return miles

if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie)
    print(result)

