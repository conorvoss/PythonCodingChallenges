'''
Created on Mar 24, 2025

@author: bigcv
'''
#!/bin/python3

def caesarCipher(s, k):
    k = k % 26
    a_lower = "abcdefghijklmnopqrstuvwxyz"
    a_upper = a_lower.upper()
    a_lower_shift = a_lower[k:] + a_lower[:k]
    a_upper_shift = a_lower_shift.upper()
    
    shift = dict()
    for a in range(26):
        shift.update({a_lower[a]: a_lower_shift[a]})
        shift.update({a_upper[a]: a_upper_shift[a]})
        
    return "".join([shift.get(s[i], s[i]) for i in range(len(s))])
        

if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result + '\n')

