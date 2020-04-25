'''
Problem Statement - https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem
'''

import math

def cumulative_distribution(x,mean,sd):
    return float((0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5))))))

if __name__=='__main__':
    max=250
    no=100
    mean=2.4
    sd=2.0
    mean1 = no * mean
    sd1 = math.sqrt(no) * sd
    print('{:.4f}'.format(cumulative_distribution(max,mean1,sd1)))
