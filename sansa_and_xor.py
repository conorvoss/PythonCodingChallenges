'''
Created on Mar 26, 2025

@author: bigcv
'''
#!/bin/python3

def sansaXor(arr):
    if len(arr) % 2 == 0:
        return 0
    
    result = 0
    for i in range(0, len(arr)):
        if i % 2 == 0:
            result ^= arr[i]
    return result

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)
        print(str(result) + '\n')
