from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def level_order_traversal(self):
        #Formalities/Edge cases
        if self.root is None:
            return []

        result = [] 
        q = deque()
        q.append(self.root)
        while q:
            level_nodes = []
            level_size = len(q)

            for _ in range(level_size):
                curr = q.popleft()
                level_nodes.append(curr.data)
            #curr = q.popleft()
            #result.append(curr.data)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result .append(level_nodes)
        return result        
    def levels(self):
        result = self.level_order_traversal()
        return len(result)
    
    def preorder_traversal(self, root):
        #formalities
        if root is None:
            return []
        
        result = []
        result.append(root.data)
        result.extend(self.preorder_traversal(root.left))
        result.extend(self.preorder_traversal(root.right))
        return result
    
    def inorder_traversal(self, root):
        #formalities
        if root is None:
            return []
        
        result = []
        result.extend(self.inorder_traversal(root.left))
        result.append(root.data)
        result.extend(self.inorder_traversal(root.right))
        return result
    
    def postorder_traversal(self, root):
        #formalities
        if root is None:
            return []
        
        result = []
        result.extend(self.postorder_traversal(root.left))
        result.extend(self.postorder_traversal(root.right))
        result.append(root.data)
        return result
        pass   

tree = BinaryTree()

tree.root = Node(10)
tree.root.left = Node(12)
tree.root.right = Node(32)
tree.root.left.left = Node(34)
tree.root.right.left = Node(25)
tree.root.right.left.right = Node(7)

print(tree.level_order_traversal())
print(tree.levels())
print(tree.preorder_traversal(tree.root))
print(tree.inorder_traversal(tree.root))
print(tree.postorder_traversal(tree.root))