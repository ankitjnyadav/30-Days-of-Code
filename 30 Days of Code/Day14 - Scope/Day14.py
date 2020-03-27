'''
Problem Statement - https://www.hackerrank.com/challenges/30-scope/problem
'''
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0


    # ---  First Way ---
    def computeDifference_1(self):
        for i in range(len(a)):
            for j in range(len(a)):
                diff= abs(a[j] - a[i])
                #print('{}-{}={}'.format(a[j],a[i],diff))
                if diff>self.maximumDifference:
                    self.maximumDifference= diff

    # ---  Second Way ---
    def computeDifference_2(self):
        x=0
        while x<len(a)-1:
            for y in range(len(a)):
                diff = abs(a[x] - a[y])
                #print('{}-{}={}'.format(a[x],a[y],diff))
                if diff > self.maximumDifference:
                    self.maximumDifference = diff
            x = x + 1
    # Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)