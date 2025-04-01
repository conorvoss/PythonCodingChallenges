'''
Created on Mar 26, 2025

@author: bigcv
'''
#!/bin/python3

def gridChallenge(grid):
    sort1 = [0] * 26
    sort2 = [0] * 26
    count1 = len(grid)
    count2 = 0
    for s in grid:
        for c in s:
            sort2[ord(c) - 97] += 1
        for j in range(26):
            count1 += sort1[j]
            count2 += sort2[j]
            sort1[j] = sort2[j]
            sort2[j] = 0
            if count2 > count1:
                return "NO"
        count1 = 0
        count2 = 0
    return "YES"


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result + '\n')
