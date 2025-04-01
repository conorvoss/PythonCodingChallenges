'''
Created on Mar 24, 2025

@author: bigcv
'''
#!/bin/python3

def closestNumbers(arr):
    arr.sort()
    min_dif = abs(arr[1] - arr[0])
    mins = [arr[0], arr[1]]
    for i in range(2, len(arr)):
        dif = abs(arr[i] - arr[i - 1])
        if dif == min_dif:
            mins.append(arr[i -1])
            mins.append(arr[i])
        elif dif < min_dif:
            min_dif = dif
            mins.clear()
            mins.append(arr[i -1])
            mins.append(arr[i])
    return mins
            

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)
    print(' '.join(map(str, result)))
