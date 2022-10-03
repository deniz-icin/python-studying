import math
import os
import random
import re
import sys



def solve(meal_cost, tip_percent, tax_percent):
    last_cost = meal_cost + (meal_cost * tip_percent / 100) + (meal_cost * tax_percent / 100)
    print(round(last_cost))