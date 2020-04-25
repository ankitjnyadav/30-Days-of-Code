'''
Problem Statement - https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
'''
import math

def cumulative_distribution(x,mean,sd):
    return float(100*(0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5))))))

if __name__ == '__main__':
    mean, sd = map(float, input().split())
    x = float(input())
    y = float(input())
    p1 = float(100) - cumulative_distribution(x,mean,sd)
    p2 = float(100) - cumulative_distribution(y,mean,sd)
    p3 = float(cumulative_distribution(y,mean,sd))
    print('{:.2f}'.format(p1))
    print('{:.2f}'.format(p2))
    print('{:.2f}'.format(p3))


