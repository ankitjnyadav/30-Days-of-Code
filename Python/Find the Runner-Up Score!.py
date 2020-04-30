'''
Problem Statement - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr,reverse=True)
    for i in range(len(arr)):
        if arr[i]!=arr[i+1]:
            print(arr[i+1])
            break