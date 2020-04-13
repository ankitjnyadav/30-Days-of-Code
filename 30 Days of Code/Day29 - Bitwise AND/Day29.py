'''
Problem Statement - https://www.hackerrank.com/challenges/30-bitwise-and/problem
'''

import math
import os
import random
import re
import sys


def bitwise(n,k):
    max = 0
    for i in range(n,1,-1):
        for j in range(i-1,0,-1):
            res = i & j
            if res > max and res < k:
                max = res
            if max == k-1:
                break
        if max == k-1:
            break
    return(max)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(bitwise(n,k))