'''
Created on Mar 27, 2025

@author: bigcv
'''
#!/bin/python3

print(int("sss"))

def formingMagicSquare(s):
    magic_squares = [[[8,3,4],[1,5,9],[6,7,2]],
                     [[6,1,8],[7,5,3],[2,9,4]],
                     [[2,7,6],[9,5,1],[4,3,8]],
                     [[4,9,2],[3,5,7],[8,1,6]],
                     [[4,3,8],[9,5,1],[2,7,6]],
                     [[8,1,6],[3,5,7],[4,9,2]],
                     [[6,7,2],[1,5,9],[8,3,4]],
                     [[2,9,4],[7,5,3],[6,1,8]]]
    min_dif = 100
    winner = []
    for sq in magic_squares:
        dif = 0
        for i in range(3):
            for j in range(3):
                dif += abs(sq[i][j] - s[i][j])
        if dif < min_dif:
            min_dif = dif
            winner = sq
    print(winner)
    return min_dif


if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(str(result) + '\n')
