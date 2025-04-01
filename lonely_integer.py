'''
Created on Mar 20, 2025

@author: bigcv
'''
#!/bin/python3

def lonelyinteger(a):
    for x in a:
        if a.count(x) == 1:
            return x


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    
    result = lonelyinteger(a)
    print(str(result) + '\n')
