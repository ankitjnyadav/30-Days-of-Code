'''
Problem Statement - https://www.hackerrank.com/challenges/30-2d-arrays/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

hour_glass_sum = []

def print_stack(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            print(arr[x][y],end=" ")
        print(end="\n")

def find_hour_glass_sum(arr,row_start,colum_start):
    sum = 0
    for x in range(row_start,row_start+3):
        #print("\n")
        if x==row_start+1:
            #print(arr[x][1], end=" ")
            #int((row_start+3)/2)
            sum=sum+arr[x][colum_start+1]
        else:
            for y in range(colum_start,colum_start+3):
                #print(arr[x][y],end=" ")
                sum=sum+arr[x][y]
    #print('sum=',sum)
    return sum

def find_max_hour_glass_sum(hour_glass_sum):
    hour_glass_sum.sort(reverse = True)
    return hour_glass_sum[0]


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for x in range(len(arr)):
        if x not in range(-9,10):
            exit(0)
    for x in range(len(arr)-2):
        for y in range(len(arr)-2):
            hour_glass_sum.append(find_hour_glass_sum(arr,x,y))
    print(hour_glass_sum)
    print(find_max_hour_glass_sum(hour_glass_sum))

