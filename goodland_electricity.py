'''
Created on Apr 2, 2025

@author: bigcv
'''
#!/bin/python3

def pylons(k, arr):
    last_one = -k
    last_k = -k
    counter = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            last_one = i
        if (i - 2 * (k - 1) > last_k or 
            (i == len(arr) - 1 and i - k >= last_k)):
            if last_one > last_k:
                last_k = last_one
                counter += 1
            else:
                return -1
    return counter

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    
    result = pylons(k, arr)
    print(str(result) + '\n')

