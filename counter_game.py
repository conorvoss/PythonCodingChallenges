'''
Created on Apr 1, 2025

@author: bigcv
'''
#!/bin/python3

from math import log2

def counterGame(n):
    p = int(log2(n))
    if p != log2(n):
        return counterGame(2 *(n - 2 ** p))
    
    if p % 2 == 0:
        return "Richard"
    else:
        return "Louise"

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)
        print(result + '\n')
