'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3

def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1
    return count
    

if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(str(result) + '\n')
