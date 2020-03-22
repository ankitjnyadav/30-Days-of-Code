'''
Problem Statement - https://www.hackerrank.com/challenges/30-binary-numbers/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = 439
    bin_a = bin(n)
    def find_con(bin_num):
        max = 0
        count = 0
        for x in range(len(bin_num)):
            if bin_num[x]=='1' and x<len(bin_num)-1:
                count=count+1
            elif bin_num[x]=='0':
                if max<count:
                    max=count
                count=0
            elif bin_num[x]=='1' and x==len(bin_num)-1:
                count = count + 1
                if max<count:
                    max=count
        print(max)



    bin_a=bin_a.split('0b')[1]
    find_con(bin_a)

