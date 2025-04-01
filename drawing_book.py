'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3

def pageCount(n, p):
    front = p // 2
    if n % 2 == 0:
        back = (n - p) // 2
    else:
        back = (n - p + 1) // 2
    return min(front, back)        

if __name__ == '__main__':
    n = int(input().strip())
    p = int(input().strip())

    result = pageCount(n, p)
    print(str(result) + '\n')

