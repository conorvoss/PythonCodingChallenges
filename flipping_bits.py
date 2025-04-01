'''
Created on Mar 20, 2025

@author: bigcv
'''
#!/bin/python3

def flippingBits(n):
    mask = (1 << 32) - 1
    return n ^ mask


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        print(str(result) + '\n')
