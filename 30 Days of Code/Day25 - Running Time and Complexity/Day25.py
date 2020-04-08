'''
Problem Statement - https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
'''
# for (i = 2; i*i <= n; i++){
#     //if divisible
#     if (n % i == 0)
#         NOT PRIME
# }

#arr = list(map(int, input().rstrip().split()))
arr = []
n = int(input())
def check_prime_no_slow(no):
    if no>1:
        for i in range(2,no//2):
            if no%i==0:
                print('Not prime')
                break
        else:
            print('Prime')
    else:
        print('Not prime')

def check_prime_no(n):
    if n==1:
        print('Not prime')
    else:
        square_root = int(n ** 0.5)
        for i in range(2, square_root + 1):
            if ((n % i) == 0) and (i != n):
                print('Not prime')
                break
        else:
            print('Prime')

for i in range(n):
    arr.append(int(input()))
    check_prime_no(arr[-1])

# for i in range(len(arr)):
#     check_prime_no(arr[i])

