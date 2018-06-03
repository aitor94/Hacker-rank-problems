#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    best_div = 0
    for i in reversed(range(1, n+1)):
        if n % i == 0:
            sum_num = sum(map(int,list(str(i))))
            sum_best = sum(map(int,list(str(best_div))))
            if sum_num > sum_best or (sum_num==sum_best and i<best_div):
                best_div = i
    print(best_div)
