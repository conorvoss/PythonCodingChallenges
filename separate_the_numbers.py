'''
Created on Mar 24, 2025

@author: bigcv
'''
#!/bin/python3

def recursive(num, s):
    end = 1
    while end <= len(s):
        if s[0] == "0" or num + 1 < int(s[:end]):
            return None
        elif num + 1 == int(s[:end]):
            if end == len(s):
                return [int(s[:end])]
            else:
                temp = recursive(int(s[:end]), s[end:])
                if temp is None:
                    return None
                else:
                    temp.insert(0, int(s[:end]))
                    return temp
        end += 1
    return None
            

def separateNumbers(s):
    end = 1
    while end <= len(s) // 2:
        nums = recursive(int(s[:end]), s[end:])
        if nums is not None:
            print("YES", s[:end])
            break
        
        end += 1
    else:
        print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
