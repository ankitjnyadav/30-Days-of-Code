'''
Problem Statement - https://www.hackerrank.com/challenges/s10-standard-deviation/problem
'''

import math

def decimal_print(value):
    formatted_float = "{:.1f}".format(value)
    print(formatted_float)


def calc_mean(numbers):
    mean=0
    for x in range(len(numbers)):   mean=mean+numbers[x]
    mean = mean/len(numbers)
    return mean


def cal_standar_deviation(numbers):
    mean = calc_mean(numbers)
    sum = 0
    for i in numbers:
        sum = sum + abs((i-mean)**2)
    sd = math.sqrt(sum/len(numbers))
    decimal_print(sd)



if __name__ == '__main__':
    no_of_inputs = int(input())
    numbers = list(map(int, input().rstrip().split()))
    cal_standar_deviation(numbers)