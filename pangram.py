'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3


def pangrams(s):
    letters = set(s.lower().replace(" ", ""))
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    s = input()

    result = pangrams(s)
    print(result + '\n')
