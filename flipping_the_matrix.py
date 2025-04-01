'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3

def flippingMatrix(matrix):
    dim = int(len(matrix) / 2)
    n = [[0 for _ in range(dim)] for _ in range(dim)]
    for x in range(dim):
        for y in range(dim):
            n[x][y] = max(matrix[x][y], 
                          matrix[x][2 * dim - 1 - y], 
                          matrix[2 * dim - 1 - x][y], 
                          matrix[2 * dim - 1 - x][2 * dim - 1 - y])
    return sum(sum(sublist) for sublist in n)

    
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(str(result) + '\n')
