'''
Problem Statement - https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
'''
import math


def cumulative_distribution(x,mean,sd):
    return round(0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5)))),3)

if __name__ == '__main__':
    mean, sd = map(float, input().split())
    x = float(input())
    y1, y2 = map(float, input().split())
    print(cumulative_distribution(x,mean,sd))
    print(cumulative_distribution(y2,mean,sd)-cumulative_distribution(y1,mean,sd))