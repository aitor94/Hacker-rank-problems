#!/bin/python3

import os
import sys

#
# Complete the dynamicArray function below.
#
def dynamicArray(n, queries):
    #
    # Write your code here.
    #
    answers = []
    seqs = []
    for i in range(n):
        seqs.append([])
    last_answer = 0
    for query in queries:
        sequence = seqs[(query[1] ^ last_answer) % n]
        if query[0] == 1:
                sequence.append(query[2])
        else:
            el = query[2] % len(sequence)
            answers.append(sequence[el])
            last_answer = sequence[el]
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

