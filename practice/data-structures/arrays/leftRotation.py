#!/bin/python3

import os
import sys

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    print(' '.join(str(e) for e in (a[d:] + a[:d])))

