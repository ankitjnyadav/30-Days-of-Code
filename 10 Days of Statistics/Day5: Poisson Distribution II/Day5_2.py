'''
Problem Statement - https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem
'''

'''

    e: A constant equal to approximately 2.71828. (Actually, e is the base of the natural logarithm system.)
    μ: The mean number of successes that occur in a specified region.
    x: The actual number of successes that occur in a specified region.
    P(x; μ): The Poisson probability that exactly x successes occur in a Poisson experiment, when the mean number of successes is μ.

    Poisson Formula. Suppose we conduct a Poisson experiment, in which the average number of successes within a given region is μ. Then, the Poisson probability is:
    P(x; μ) = (e^ -μ) (μ^ x) / x!
    where x is the actual number of successes that result from the experiment, and e is approximately equal to 2.71828.

'''

from math import factorial
from math import e


def cal_poisson_distribution(mean,actual_no):
    return (e**-mean)*(mean**actual_no)/factorial(actual_no)

def decimal_print(value):
    formatted_float = "{:.3f}".format(value)
    print(formatted_float)

if __name__ == "__main__":
    mean = float(input())
    actual_no = float(input())
    decimal_print(cal_poisson_distribution(mean,actual_no))


