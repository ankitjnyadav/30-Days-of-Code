'''
Problem Statement - https://www.hackerrank.com/challenges/30-binary-trees/problem
'''

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def printOrder(self,curr):
        print('*'*20)
        #print(curr.data)
        #print(curr.left.data,curr.right.data)
        if curr.left != None:
            print(curr.left.data)
            return self.printOrder(curr.left)

        if curr.right!= None:
            print(curr.right.data)
            return self.printOrder(curr.right)

    def levelOrder(self, root):
        q = []
        q.append(root)
        while(len(q)>0):
            print(q[0].data,end=' ')
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)



    def levelOrder1(self,root):
        # if root.left and root.right:
        #     print(root.data)
        #     return self.levelOrder(root.left) and self.levelOrder(root.right)
        #
        print('#' * 20)
        print(root.data)
        # if root.left and root.right:
        #     self.printOrder(root)

        #


        lcurr = root.left
        rcurr = root.right
        while lcurr != None and rcurr != None:
            lcurr = lcurr.left
            rcurr = rcurr.right

        #
        #

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
