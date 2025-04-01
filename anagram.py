'''
Created on Mar 24, 2025

@author: bigcv
'''
#!/bin/python3

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2:]
    counts = dict()
    for c in s1:
        counts.update({c: counts.get(c, 0) + 1})
    dif = 0
    for c in s2:
        x = counts.get(c, 0)
        if x > 0:
            counts.update({c: x - 1})
        else:
            dif += 1
    
    return dif
    
    

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()

        result = anagram(s)
        print(str(result) + '\n')
