'''
Created on Apr 1, 2025

@author: bigcv
'''
#!/bin/python3

def superDigit(n, k):
    if len(n) == 1:
        return int(n)
    else:
        total = sum(int(d) for d in n) * k
        return superDigit(str(total), 1)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(str(result) + '\n')
