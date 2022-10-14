import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    
def weird_or_not():
    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0 and 2<=N<=5:
        print("Not Weird")
    elif N % 2 == 0 and 6<=N<=20:
        print("Weird")
    elif N % 2 == 0 and 20<N:
        print("Not Weird")

weird_or_not()
