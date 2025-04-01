'''
Created on Mar 20, 2025

@author: bigcv
'''
#!/bin/python3

def countingSort(arr):
    counts = [0] * 100
    for x in arr:
        counts[x] += 1
    return counts


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(' '.join(map(str, result)))
