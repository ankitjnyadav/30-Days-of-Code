'''
Problem Statement - https://www.hackerrank.com/challenges/30-queues-stacks/problem
'''
import sys
from collections import deque


class Stack:
    def __init__(self):
        self.__list = []

    def push(self, key):
        self.__list.append(key)

    def pop(self):
        return self.__list.pop()

    def is_empty(self):
        return len(self.__list) == 0


class Solution:
    my_stack = Stack()
    my_q = deque()

    def pushCharacter(self,ch) :
        self.my_stack.push(ch)

    def enqueueCharacter(self,ch):
        self.my_q.append(ch)

    def popCharacter(self):
        return self.my_stack.pop()

    def dequeueCharacter(self):
        return self.my_q.popleft()


# Write your code here

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
#ankit
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")