'''
Problem Statement - https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
'''

def cal_geometri_distribution(probability,no_of_occurences):
    gd = 0
    for i in range(1, no_of_occurences + 1):
        print(i)
        gd += ((1-probability)**(no_of_occurences-i))*probability
    return gd
def decimal_print(value):
    formatted_float = "{:.3f}".format(value)
    print(formatted_float)

if __name__ == "__main__":
    no1,no2 = map(int, input().split(' '))
    no_of_occurences = int(input())
    P = no1/no2
    decimal_print(cal_geometri_distribution(P,no_of_occurences))



