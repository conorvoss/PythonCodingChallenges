'''
Created on Mar 25, 2025

@author: bigcv
'''
#!/bin/python3

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    count = 0
    x = [1] * 4
    for c in password:
        count += 1
        if c in numbers:
            x[0] = 0
        elif c in lower_case:
            x[1] = 0
        elif c in upper_case:
            x[2] = 0
        elif c in special_characters:
            x[3] = 0

    return max(sum(x), 6 - count)

if __name__ == '__main__':
    n = int(input().strip())
    password = input()

    answer = minimumNumber(n, password)
    print(str(answer) + '\n')
