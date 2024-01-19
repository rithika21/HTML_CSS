# ~~1. Understand how LLs are created.~~
# ~~2. CRUD operations~~
# ~~3. Loops in LLs~~
# 4. Sort the LLs (merge sort)
# 5. Intersection in LLs
# 6. Some interesting problems
 
# Recall: Every class: Data + Functions
class Node:
    # Data
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    # Data
    def __init__(self):
        self.head = None
 
    # Functions
    def append(self, data):
        new_node = Node(data)
        # If my head is empty
        if self.head is None: 
            self.head = new_node
            return
        # If head is not empty
        last_node = self.head
        while last_node.next: 
            last_node = last_node.next
        last_node.next = new_node
 
    def merge_sort(self, head):
        # Base condition
        if not head or not head.next:
            return head
 
        # Recursive approach: Decomposition
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
 
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)
 
        # Recomposition
        sorted_list = self.merge(left, right)
        return sorted_list
    
    def get_middle(self, head):
        if not head:
            return head
    
        slow = head
        fast = head
 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
 
        # slow is at the mid
        return slow
    
    def merge(self, left, right):
        result = None
 
        if not left:
            return right
        if not right:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
 
        return result
    
    # Wrapper, because l.merge_sort(l) -> Doesnt feel good
    def sort(self):
        self.head = self.merge_sort(self.head)
 
    def print(self):
        a = self.head
        while a:
            print(a.data, end=" ")
            a = a.next  # DO NOT FORGET TO STEP FORWARD
        print()
 
 
l = LinkedList()
 
l.append(7)
l.append(2)
l.append(3)
l.append(1)
l.append(5)
l.append(4)
 
print("Before sorting: ")
l.print()
 
l.sort()
 
print("After sorting: ")
l.print()