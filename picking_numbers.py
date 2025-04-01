'''
Created on Mar 24, 2025

@author: bigcv
'''
#!/bin/python3

def pickingNumbers(a):
    count1 = 1
    count2 = 1
    max_count = 1
    pos = False
    neg = False
    running_dif = 0
    for i in range(1, len(a)):
        dif = a[i] - a[i-1]
        if abs(dif) > 1:
            count1 = 1
            count2 = 1
        elif dif == -1:
            running_dif -= 1
            neg = True
            count2 = 1
            if running_dif < -1 or (pos and running_dif < 0):
                count1 = count2
                running_dif = 0
                pos = False
                neg = False
            else:
                count1 += 1
                if count1 > max_count:
                    max_count = count1
            
        elif dif == 1:
            running_dif += 1
            pos = True
            count2 = 1
            if running_dif > 1 or (neg and running_dif > 0):
                count1 = count2
                running_dif = 0
                pos = False
                neg = False
            else:
                count1 += 1
                if count1 > max_count:
                    max_count = count1
        else:
            #dif == 0
            count1 += 1
            count2 += 1
            if count1 > max_count:
                max_count = count1
    
    return max_count
    

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(str(result) + '\n')