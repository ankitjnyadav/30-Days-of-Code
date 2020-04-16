'''
Problem Statement - https://www.hackerrank.com/challenges/s10-interquartile-range/problem
'''

def decimal_print(value):
    formatted_float = "{:.1f}".format(value)
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
    frequencies = list(map(int, input().rstrip().split()))
    data = []
    for i in range(len(numbers)):
        for j in range(frequencies[i]):
            data.append(numbers[i])

    numbers=data



    i=0
    split = []
    size = len(numbers)//2
    numbers = sorted(numbers)
    print(numbers)
    q2 = calc_median(numbers)
    while i<=size and numbers[i]<=q2:
        split.append(numbers[i])
        i=i+1
    print(split)
    q1=calc_median(split)

    split = []
    i= len(numbers)-1

    size = len(numbers)//2
    while i>size and numbers[i] >= q2:
        split.append(numbers[i])
        i = i - 1
    print(split)
    q3 = calc_median(split)
    print(q1,q2,q3)
    decimal_print(q3-q1)


