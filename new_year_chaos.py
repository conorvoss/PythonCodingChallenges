'''
Created on Apr 2, 2025

@author: bigcv
'''
#!/bin/python3

def minimumBribes(q):
    count = 1
    total_count = 0
    while count > 0:
        count = 0
        for i in range(len(q) - 1):
            if q[i] > i + 3:
                print("Too chaotic")
                return
            if q[i] > q[i + 1]:
                tmp = q[i]
                q[i] = q[i + 1]
                q[i + 1] = tmp
                count += 1
        total_count += count
    print(total_count)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
