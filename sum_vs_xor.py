'''
Created on Apr 1, 2025

@author: bigcv
'''
#!/bin/python3

def sumXor(n):
    if n == 0:
        return 1
    e = bin(n)[2:].count("0")
    return 2 ** e

if __name__ == '__main__':
    n = int(input().strip())

    result = sumXor(n)
    print(str(result) + '\n')
