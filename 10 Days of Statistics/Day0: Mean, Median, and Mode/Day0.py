'''
Problem Statement - https://www.hackerrank.com/challenges/s10-basic-statistics/problem
'''


def decimal_print(value):
    formatted_float = "{:.1f}".format(value)
    print(formatted_float)


def calc_mean(numbers):
    mean=0
    for x in range(len(numbers)):   mean=mean+numbers[x]
    mean = mean/len(numbers)
    decimal_print(mean)


def calc_median(numbers):
    median=0
    numbers = sorted(numbers)
    if len(numbers)%2==0:
        mid1 = len(numbers) // 2
        mid2 = mid1-1
        median = (numbers[mid1]+numbers[mid2])/2
        return decimal_print(median)
    else:
        mid = len(numbers) // 2
        median = numbers[mid]
        return decimal_print(median)


def calc_mode(numbers):
    mode=0
    dict = {}
    numbers = sorted(numbers)
    for x in range(len(numbers)):
        dict[numbers[x]] = numbers.count(numbers[x])
    print(dict)
    x_key = max(dict, key=dict.get)
    print(x_key)


if __name__ == '__main__':
    no_of_inputs = int(input())
    numbers = list(map(int, input().rstrip().split()))
    calc_mean(numbers)
    calc_median(numbers)
    calc_mode(numbers)



