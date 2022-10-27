import math
import os
import random
import re
import sys
import string

if __name__ == '__main__':
    
    N = int(input().strip())
    firstName_list = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        firstName_list.append(firstName)
        emailID = first_multiple_input[1]

    for _ in firstName_list:
        for i in _:
            a = list(string.ascii_lowercase)
            b = ["@","."]
            assert i in a or b, "First names consists of lower case letters a-z only."
    assert 2<=N<=30, "Total number of rows should be in range of 2 and 30."
    assert len(firstName) <= 20, "The length of the first name is no longer than 20"
    assert len(emailID) <= 50, "The length of the email ID is no longer than 50"
    
    sorted_list = sorted(firstName_list)
    
    for _ in sorted_list:
        print(_)
    