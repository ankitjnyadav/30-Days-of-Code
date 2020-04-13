'''
Problem Statement - https://www.hackerrank.com/challenges/30-regex-patterns/problem
'''

import re

if __name__ == '__main__':
    N = int(input())
    pattern = '.+@gmail\.com'
    name = []
    for N_itr in range(N):
        first_name_email_id = input().split()
        firstName = first_name_email_id[0]
        emailID = first_name_email_id[1]
        result1 = re.match(pattern, emailID)
        if result1:
            name.append(firstName)

    name.sort(reverse=False)
    for ele in name:
        print(ele)