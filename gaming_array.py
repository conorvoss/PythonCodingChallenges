'''
Created on Mar 27, 2025

@author: bigcv
'''
#!/bin/python3

def gamingArray(arr):
    max_val = 0
    turns = 0
    for x in arr:
        if x > max_val:
            max_val = x
            turns += 1
    if turns % 2 == 0:
        return "ANDY"
    else:
        return "BOB"
    

if __name__ == '__main__':
    g = int(input().strip())
    for g_itr in range(g):
        arr_count = int(input().strip())
        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)
        print(result + '\n')
