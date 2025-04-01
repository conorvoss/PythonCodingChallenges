'''
Created on Mar 20, 2025

@author: bigcv
'''
#!/bin/python3

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    count = 0
    
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
        count += 1
    
    print(f"{pos / count:.6f}")
    print(f"{neg / count:.6f}")
    print(f"{zero / count:.6f}")

if __name__ == '__main__':
    
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
