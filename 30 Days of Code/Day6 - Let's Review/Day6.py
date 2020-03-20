'''
Problem Statement:
'''


list = []
n = int(input())
for x in range(n):
    y = input()
    list.insert(x,y)
for x in list:
    print(x[::2], x[1::2])
