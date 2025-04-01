'''
Created on Mar 26, 2025

@author: bigcv
'''
#!/bin/python3

def missingNumbers(arr, brr):
    min_brr = min(brr)
    counts = [0] * 101
    for x in brr:
        counts[x - min_brr] += 1
    for x in arr:
        counts[x-min_brr] -= 1
        
    return [i + min_brr for i in range(100) if counts[i] > 0]      

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)
    print(' '.join(map(str, result)))
