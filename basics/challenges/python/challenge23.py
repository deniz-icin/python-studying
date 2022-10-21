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

    def levelOrder(self,root):
        line = [root]
        values = []
        
        while line:
            new_node = line.pop(0)
            values.append(new_node.data)
            
            if new_node.left:
                line.append(new_node.left)
                
            if new_node.right:
                line.append(new_node.right)
                
        print(*values)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
