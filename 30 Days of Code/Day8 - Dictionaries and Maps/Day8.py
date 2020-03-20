'''
Problem Statement:
'''

import sys

n = 0
phoneBook = dict()
n = int(input())

for x in range(n):
    value = input()
    if len(value.split()) == 2:
        k, v = value.split()
        phoneBook[k] = v

flag = True
user_inputs= []

while flag:
    name = sys.stdin.readline().rstrip()
    user_inputs.append(name)
    if len(user_inputs[-1]) == 0:
        flag = 0
    else:
        if name not in phoneBook:
            print('Not found')
        else:
            print(name, '=', phoneBook[name], sep='')
