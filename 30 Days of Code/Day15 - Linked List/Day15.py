'''
Problem Statement - https://www.hackerrank.com/challenges/30-linked-list/problem
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        current_node = Node(data)
        first=head
        if head==None:
            head = current_node
        else:
            while first.next != None:
                first = first.next
            first.next = current_node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);