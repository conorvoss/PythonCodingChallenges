'''
Created on Mar 22, 2025

@author: bigcv
'''
#!/bin/python3

#from timeit import timeit

#my_setup = '''

from functools import reduce
from random import randint

loop_count1 = 0
loop_count2 = 0

def getTotalX_firstattempt(a, b):
    global loop_count1
    count = 0
    a.sort()
    b.sort()
    min_num = a[-1]
    max_num = b[0]
    while min_num % a[0] != 0:
        min_num += 1
        loop_count1 += 1
    
    for num in range(min_num, max_num + 1, a[0]):
        fail = False
        for x in a:
            loop_count1 += 1
            if num % x != 0:
                fail = True
                break
        if fail:
            continue
        for y in b:
            loop_count1 += 1
            if y % num != 0:
                fail = True
                break
        if not fail:
            count += 1
    
    return count

def gcd(a, b):
    global loop_count2
    while b:
        loop_count2 += 1
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a,b)

def getTotalX(a, b):
    global loop_count2
    max_num = reduce(gcd, b)
    min_num = 1
    for x in a:
        loop_count2 += 1
        min_num = lcm(x, min_num)
        if min_num > max_num or max_num % min_num != 0:
            return 0
    
    count = 1
    for num in range(min_num * 2, max_num + 1, min_num):
        loop_count2 += 1
        if max_num % num == 0:
            count += 1
    
    return count

def get_totals1(random_lists):
    totals = list()
    for a, b in random_lists:
        totals.append(getTotalX_firstattempt(a, b))
    print(totals)
     
def get_totals2(random_lists):
    totals = list()
    for a, b in random_lists:
        totals.append(getTotalX(a, b))
    print(totals)



number_of_lists = 10
random_lists = []

for _ in range(number_of_lists):
    list_length = randint(2, 10000)
    random_list1 = [randint(2, 3) for _ in range(list_length - 1)]
    random_list2 = [randint(10, 13) for _ in range(list_length)]
    random_lists.append((random_list1, random_list2))



'''

time1 = timeit(setup=my_setup, stmt="get_totals1(random_lists)", number=10000)
time2 = timeit(setup=my_setup, stmt="get_totals2(random_lists)", number=10000)

print(f"time 1: {time1}")
print(f"time 2: {time2}")

'''
    
get_totals1(random_lists)
get_totals2(random_lists)



print(loop_count1, loop_count2)
