'''
Problem Statement - https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem
'''
'''
The Geometric Distribution
Geometric distribution - A discrete random variable X is said to have a geometric distribution if it has a probability density function (p.d.f.) of the form:

(1-P)**r-1 * P
'''
def cal_geometri_distribution(probability,no_of_occurences):
    return ((1-probability)**(no_of_occurences-1))*probability

def decimal_print(value):
    formatted_float = "{:.3f}".format(value)
    print(formatted_float)

if __name__ == "__main__":
    no1,no2 = map(int, input().split(' '))
    no_of_occurences = int(input())
    P = no1/no2
    decimal_print(cal_geometri_distribution(P,no_of_occurences))



