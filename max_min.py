'''
Created on Mar 25, 2025

@author: bigcv
'''
#!/bin/python3

def maxMin(k, arr):
    arr.sort()
    min_unf = arr[-1] - arr[0]
    k -= 1
    for i in range(k, len(arr)):
        if arr[i] - arr[i - k] < min_unf:
            min_unf = arr[i] - arr[i - k]
    
    return min_unf
        

if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(str(result) + '\n')
