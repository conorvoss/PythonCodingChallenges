'''
Created on Mar 20, 2025

@author: bigcv
'''
#!/bin/python3

def gradingStudents(grades):
    return [x if x <= 37 
            else x + 5 - x % 5 if x % 5 >= 3 
            else x for x in grades]

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))

