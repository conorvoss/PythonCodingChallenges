'''
Created on Apr 2, 2025

@author: bigcv
'''
#!/bin/python3

def bomberMan(n, grid):
    maxr = len(grid)
    maxc = len(grid[0])
    if n % 2 == 0:
        return ["O" * maxc for _ in grid]
    elif n == 1:
        return grid
    else:
        grid = [[c for c in r] for r in grid]
        for _ in range(2 - ((n // 2) % 2)):
            temp = [["O" for _ in range(maxc)] for _ in range(maxr)]
            for r in range(maxr):
                for c in range(maxc):
                    if grid[r][c] == "O":
                        temp[r][c] = "."
                        temp[max(0, r - 1)][c] = "."
                        temp[min(maxr - 1, r + 1)][c] = "."
                        temp[r][max(0, c - 1)] = "."
                        temp[r][min(maxc - 1, c + 1)] = "."
            grid = temp.copy()
        return ["".join(r) for r in grid]
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])
    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    print('\n'.join(result))
    print('\n')

