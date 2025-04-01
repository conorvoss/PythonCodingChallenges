'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3

def marsExploration(s):
    count = 0
    for i in range(len(s)):
        if i % 3 == 1:
            if s[i] != "O":
                count += 1
        elif s[i] != "S":
            count += 1
    return count

if __name__ == '__main__':
    s = input()

    result = marsExploration(s)
    print(str(result) + '\n')
