import math
import os
import random
import re
import sys
from itertools import combinations as comb

def bitwiseAnd(N, K):
    answer = max(a&b for a, b in comb(range(K-2, N+1), 2) if a&b < K)
    return answer

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
