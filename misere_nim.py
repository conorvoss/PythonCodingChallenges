'''
Created on Mar 27, 2025

@author: bigcv
'''
#!/bin/python3
def misereNim(s):
    if all(x == 1 for x in s):
        if len(s) % 2 == 1:
            return "Second"
        else:
            return "First"
    else:
        balance = 0
        for val in s:
            balance ^= val
        if balance == 0:
            return "Second"
        else:
            return "First"

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)
        print(result + '\n')
