'''
Created on Apr 2, 2025

@author: bigcv
'''
#!/bin/python3

def isValid(s):
    counts = {}
    for c in s:
        counts.update({c : counts.get(c, 0) + 1})
    
    vals = sorted(counts.values())
    y = vals[0]
    r = 0
    for x in vals:
        if x > y:
            if r == 0 and x - 1 == y:
                r += 1
            else:
                return "NO"
    return "YES"
            
        

if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print(result + '\n')
