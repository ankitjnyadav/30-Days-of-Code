'''
Problem Statement - https://www.hackerrank.com/challenges/s10-quartiles/problem
'''

def decimal_print(value):
    formatted_float = "{:.0f}".format(value)
    print(formatted_float)


def calc_median(numbers):
    median=0
    if len(numbers)%2==0:
        mid1 = len(numbers) // 2
        mid2 = mid1-1
        median = (numbers[mid1]+numbers[mid2])/2
        return median
    else:
        mid = len(numbers) // 2
        median = numbers[mid]
        return median



if __name__ == '__main__':
    no_of_inputs = int(input())
    numbers = list(map(int, input().rstrip().split()))
    numbers = sorted(numbers)
    q2 = calc_median(numbers)

    i=0
    split = []
    while numbers[i]<q2:
        split.append(numbers[i])
        i=i+1
    q1=calc_median(split)

    split = []
    i= len(numbers)-1
    while numbers[i] > q2:
        split.append(numbers[i])
        i = i - 1
    q3 = calc_median(split)

    decimal_print(q1)
    decimal_print(q2)
    decimal_print(q3)