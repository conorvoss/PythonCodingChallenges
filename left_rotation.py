'''
Created on Mar 24, 2025

@author: bigcv
'''
#!/bin/python3

def rotateLeft(d, arr):
    arr.extend(arr[:d])
    return arr[d:]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)
    print(' '.join(map(str, result)))
