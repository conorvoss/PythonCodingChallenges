'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3

def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse = True)
    for i in range(len(sticks) - 2):
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            return [sticks[i + 2], sticks[i + 1], sticks[i]]
    return [-1]

if __name__ == '__main__':
    n = int(input().strip())
    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
    print(' '.join(map(str, result)))
