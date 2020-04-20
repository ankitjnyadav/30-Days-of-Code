'''
Problem Statement - https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
'''

from math import factorial

def bionomial_distro(x, n, p):
    factional_part = factorial(n)/(factorial(x)*factorial(n-x))
    result =factional_part*p**x*(1-p)**(n-x)
    return result


if __name__ == "__main__":
    rej_per,n = map(int, input().split(' '))
    p = rej_per/100
    ans1 = 0
    ans2=0
    for x in range(3):
        ans1+= bionomial_distro(x, n, p)
    print(round(ans1,3))

    for x in range(2,n+1):
        ans2+= bionomial_distro(x, n, p)
    print(round(ans2,3))