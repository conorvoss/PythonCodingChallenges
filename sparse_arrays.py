'''
Created on Mar 20, 2025

@author: bigcv
'''
#!/bin/python3

def matchingStrings(strings, queries):
    return [strings.count(x) for x in queries]


if __name__ == '__main__':
    strings_count = int(input().strip())
    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())
    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))
