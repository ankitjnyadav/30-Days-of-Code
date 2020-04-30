'''
Problem Statement - https://www.hackerrank.com/challenges/nested-list/problem
'''

if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.update({name:score})

    min_score = 0
    sorted_scores = sorted(students.values())
    for i in range(len(sorted_scores)):
        if sorted_scores[i]!=sorted_scores[i+1]:
            min_score = sorted_scores[i+1]
            break
    def get_key(val):
        keylist=[]
        for key, value in students.items():
            if value == min_score:
                keylist.append(key)
        for i in sorted(keylist): print(i)
    get_key(min_score)