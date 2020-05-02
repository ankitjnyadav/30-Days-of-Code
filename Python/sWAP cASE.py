'''
Problem Statement - https://www.hackerrank.com/challenges/swap-case/problem
'''

def swap_case(s):
    result = ''
    for i in range(len(s)):
        if s[i].isupper():
            result+=s[i].lower()
        elif s[i].islower():
            result+=s[i].upper()
        else:
            result+= s[i]
    return result

if __name__ == '__main__':
    s = 'Pythonist 2' # → pYTHONIST 2input()
    result = swap_case(s)
    print(result)