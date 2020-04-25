'''
Problem Statement - https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem
'''

import math

if __name__=='__main__':
    mean = 500
    std = 80
    n = 100
    zScore = 1.96
    marginOfError = float(zScore*std/math.sqrt(n))

    print('{:.2f}\n{:.2f}'.format(mean - marginOfError, mean + marginOfError))
