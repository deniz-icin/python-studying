import math
import os
import random
import re
import sys


def bitwiseAnd(N, K):
    all_results = []
    max_possible = []
    for i in range(1,N):
        for ii in range(2,N+1):
            if ii > i:
                result = i & ii
                all_results.append(result)
    for _ in all_results:
        if _ < K:
            max_possible.append(_)
            result = max(max_possible)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
