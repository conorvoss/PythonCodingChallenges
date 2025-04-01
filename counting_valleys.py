'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3

def countingValleys(steps, path):
    count = 0
    elevation = 0
    in_valley = False
    
    for i in path:
        if i == "U":
            elevation += 1
        else:
            elevation -= 1
            
        if elevation == -1 and not in_valley:
            count +=1
            in_valley = True
        elif elevation == 0:
            in_valley = False
    
    return count
            

if __name__ == '__main__':
    steps = int(input().strip())
    path = input()

    result = countingValleys(steps, path)
    print(str(result) + '\n')
