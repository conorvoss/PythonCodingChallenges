'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3

def migratoryBirds(arr):
    counts = {}
    for i in arr:
        counts[i] = counts.get(i, 0) + 1
    bird_id = 0
    max_count = 0
    for bird in counts:
        if counts[bird] > max_count:
            max_count = counts[bird]
            bird_id = bird
        elif counts[bird] == max_count and bird < bird_id:
            bird_id = bird
    return bird_id


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(str(result) + '\n')
