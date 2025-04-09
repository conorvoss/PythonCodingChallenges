'''
Created on Apr 1, 2025

@author: bigcv
'''
#!/bin/python3

def checkpalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def palindromeIndex(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            if checkpalindrome(s[:l] + s[l+1:]):
                return l
            elif checkpalindrome(s[:r] + s[r+1:]):
                return r
            else:
                return -1
        l += 1
        r -= 1
    return -1

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(str(result) + '\n')

