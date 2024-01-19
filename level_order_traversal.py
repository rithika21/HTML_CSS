from collections import deque


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def level_order_traversal(self):
        #formality / edge cases:
        if self.root is None:
            return []
        
        
        result=[]
        q=deque()
        q.append(self.root)
        
        while q:
            curr=q.popleft()
            result.append(curr.data)
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        return result
        pass
        
        
        
        
tree=BinaryTree()

tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.right.left=Node(5)

print(tree.level_order_traversal())