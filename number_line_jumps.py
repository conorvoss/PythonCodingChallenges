'''
Created on Mar 24, 2025

@author: bigcv
'''
#!/bin/python3

def kangaroo(x1, v1, x2, v2):
    if v2 >= v1:
        return "NO"
    else:
        return (x2 - x1) % (v2 - v1) == 0

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result + '\n')