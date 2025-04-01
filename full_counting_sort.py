'''
Created on Mar 26, 2025

@author: bigcv
'''
#!/bin/python3

def countSort(arr):
    sort = [[] for _ in range(100)]
    h = len(arr) // 2
    for i in range(len(arr)):
        if i < h:
            sort[int(arr[i][0])].append("-")
        else:
            sort[int(arr[i][0])].append(arr[i][1])
    
    print(" ".join(x for sublist in sort for x in sublist))   

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
