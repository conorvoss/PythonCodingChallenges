'''
Created on Mar 27, 2025

@author: bigcv
'''
#!/bin/python3

import sys

def fibonacciModified(t1, t2, n):
    for _ in range(n-2):
        temp = t1 + t2 ** 2
        t1 = t2
        t2 = temp
    
    return temp
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    t1 = int(first_multiple_input[0])
    t2 = int(first_multiple_input[1])
    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)
    sys.set_int_max_str_digits(1000000)
    print(str(result) + '\n')

