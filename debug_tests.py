'''
Created on Mar 24, 2025

@author: bigcv
'''

from functools import reduce


def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a
    
    
a = [15, 30, 25, 100, 10, 99]

num = reduce(gcd, a)

print(num)

for x in range(400, 300, 100):
    print("rsdfsd")

import random

number_of_lists = 100
list_length = 10
random_lists = []

for _ in range(number_of_lists):
    random_list = [random.randint(1, 100) for _ in range(list_length)]
    random_lists.append(random_list)

# Printing the first 5 lists as an example
for i in range(5):
    print(f"List {i+1}: {random_lists[i]}")