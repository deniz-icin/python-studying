import math
import os
import random
import re
import sys
import string

if __name__ == '__main__':
    
    N = int(input().strip())
    firstName_list = []
    email_list = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        x = emailID.split("@")

        if x[1] == "gmail.com":
            firstName_list.append(firstName)

    for _ in firstName_list:
        for __ in _:
            a = list(string.ascii_lowercase)
            b = ["@","."]
            assert __ in a or b, "First names consists of lower case letters a-z only."
    assert 2<=N<=30, "Total number of rows should be in range of 2 and 30."
    assert len(firstName) <= 20, "The length of the first name is no longer than 20"
    assert len(emailID) <= 50, "The length of the email ID is no longer than 50"
    
    sorted_list = sorted(firstName_list)
    
    for _ in sorted_list:
        print(_)
