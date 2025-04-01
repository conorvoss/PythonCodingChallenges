'''
Created on Mar 26, 2025

@author: bigcv
'''
#!/bin/python3

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    for q in queries:
        idx = (q[1] ^ lastAnswer) % n
        if q[0] == 1:
            arr[idx].append(q[2])
        else:
            lastAnswer = arr[idx][q[2] % len(arr[idx])]
            answers.append(lastAnswer)
    return answers


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print('\n'.join(map(str, result)))
