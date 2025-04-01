'''
Created on Mar 20, 2025

@author: bigcv
'''
#!/bin/python3

def diagonalDifference(arr):
    '''
    sum1 = 0
    sum2 = 0
    for row in range(len(arr)):
        sum1 += arr[row][row]
        sum2 += arr[row][-row-1]
    return abs(sum1 - sum2)
    '''
    '''
    sum1 = sum([arr[x][x] for x in range(len(arr))])
    sum2 = sum([arr[x][-x-1] for x in range(len(arr))])
    return abs(sum1 - sum2)
    '''
    return abs(sum([arr[x][x]-arr[x][-x-1] for x in range(len(arr))]))
    
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        
    result = diagonalDifference(arr)
    print(str(result) + '\n')
