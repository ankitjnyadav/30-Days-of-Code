'''
Problem Statement - https://www.hackerrank.com/challenges/30-interfaces/problem
'''
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        i=1
        sum=0
        while i<=n:
            if n%i==0:
                sum=sum+i
            i=i+1
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)