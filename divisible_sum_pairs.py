'''
Created on Mar 20, 2025

@author: bigcv
'''
#!/bin/python3

def divisibleSumPairs(n, k, ar):
    count = 0
    for x in range(n-1):
        for y in range(x + 1, n):
            if (ar[x] + ar[y]) % k == 0:
                count +=1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar = list(map(int, input().rstrip().split()))
    
    result = divisibleSumPairs(n, k, ar)
    print(result)
