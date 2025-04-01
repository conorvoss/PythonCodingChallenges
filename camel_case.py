'''
Created on Mar 20, 2025

@author: bigcv
'''
#!/bin/python3

import sys

def split(old_list):
    new_list = [x if x.islower() 
                else " " + x.lower() 
                for x in old_list
                if (x != "(" and x != ")")]
    print("".join(new_list).strip())

def combine(name_type, old_list):
    new_list = []
    capitalize = name_type == "C"
    for x in old_list:
        
        if x == " ":
            capitalize = True
            continue
        
        if capitalize:
            x = x.upper()
            capitalize = False
            
        new_list.append(x)
    if name_type == "M":
        new_list.append("()")
    print("".join(new_list))
            

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    for line in lines:
        line = line.strip()
        if line == "":continue
        if line[0] == "S":
            split(line[4:])
        elif line[0] == "C":
            combine(line[2], line[4:])

        




