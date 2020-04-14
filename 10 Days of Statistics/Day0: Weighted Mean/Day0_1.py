'''
Problem Statement - https://www.hackerrank.com/challenges/s10-weighted-mean/problem
'''


def decimal_print(value):
    formatted_float = "{:.1f}".format(value)
    print(formatted_float)


def calc_weighted_mean(numbers,weights):
    mean=0
    weight_sum=0
    for x in range(len(numbers)):   mean,weight_sum=mean+weights[x]*numbers[x],weight_sum+weights[x]
    mean = mean/weight_sum
    decimal_print(mean)


if __name__ == '__main__':
    no_of_inputs = int(input())
    numbers = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    calc_weighted_mean(numbers,weights)