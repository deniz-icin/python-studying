import math
import os
import random
import re
import sys



def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i in range(n):
        left_to_right += arr[i][i]
    return left_to_right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()