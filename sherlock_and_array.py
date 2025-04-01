'''
Created on Mar 27, 2025

@author: bigcv
'''
#!/bin/python3

def balancedSums(arr):
    total = sum(arr)
    prog = 0
    for i in range(len(arr)):
        if total - arr[i] == prog * 2:
            return "YES"
        prog += arr[i]
    return "NO"

if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)
        print(result + '\n')
