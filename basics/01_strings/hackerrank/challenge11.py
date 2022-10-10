import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []
    max_value = -sys.maxsize
    current = 0

    
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

for i in range(4):
    for j in range(4):
        current = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
        if current >= max_value:
            max_value = current

print(max_value)    
