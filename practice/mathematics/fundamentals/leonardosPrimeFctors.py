#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primeCount(n, primes):
    #
    # Write your code here.
    #
    factor = 1
    count = 0
    for prime in primes:
        factor = factor * prime
        if factor > n:
            break
        count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    
    primes = []
    factor = 1
    n = 1
    while factor < 10**18:
        n += 1
        if is_prime(n):
            factor = factor * n 
            primes.append(n)
            
    for q_itr in range(q):
        n = int(input())

        result = primeCount(n, primes)

        fptr.write(str(result) + '\n')

    fptr.close()

