'''
Problem Statement - https://www.hackerrank.com/challenges/30-scope/problem
'''
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0

    def computeDifference(self):
        for i in range(len(a)):
            for j in range(len(a)):
                diff= abs(a[j] - a[i])
                print(diff)
                if diff>self.maximumDifference:
                    self.maximumDifference= diff

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)