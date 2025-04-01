'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3

def sockMerchant(n, ar):
    counts = {}
    for i in ar:
        counts[i] = counts.get(i, 0) + 1
    
    return sum(x // 2 for x in counts.values())

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(str(result) + '\n')
