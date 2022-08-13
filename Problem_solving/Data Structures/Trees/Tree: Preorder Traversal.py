""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 11-08-2022 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: PrepareData > Structures>Trees>Tree: Preorder Traversal
#problem link: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem?isFullScreen=false


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):
        # print(val)  
        if self.root == None:
            self.root = Node(val)
            # print('Root=> ', val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    # print('Left node==> ', val)
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        # print('Left root==> ',current.left)
                        break
                elif val > current.info:
                    # print('Right node==> ', val)
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        # print('Right root==> ',current.right)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    if root:
        print(root.info,end=" ")
        preOrder(root.left)
        preOrder(root.right)



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

# print('PreOrder: => ')
preOrder(tree.root)

