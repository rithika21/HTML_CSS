# ~~1. Understand how LLs are created.~~
# 2. CRUD operations
# 3. Loops in LLs
# 4. Sort the LLs (merge sort)
# 5. Intersection in LLs
# 6. Some interesting problems
 
# Recall: Every class: Data + Functions

###################[[https://drive.google.com/file/d/1ka6wB_STfRrMuQgB6p_GJWEVG-P8TM9-/]] ==  CLASS NOTES LINK
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
    
    def find_intersection(head1,head2):
        visited=set()

        current=head1
        while current:
            visited.add(current)
            current=current.next

        current=head2
        while current:
            if current in visited:
                return current
            current=current.next
                
 
    def print(self):
        a = self.head
        while a:
            print(a.data, end=" ")
            a = a.next  # DO NOT FORGET TO STEP FORWARD
        print()
 
 
l1 = LinkedList()

intersection_node=Node(4)

l1.append(1)
l1.append(2)
l1.append(3)
l1.next.next.next=intersection_node
l1.append(6)
l1.append(8)

l2=LinkedList()

l2.append(2)
l2.next.next=intersection_node

l1.print()
l2.print()

ins_node=l1.find_intersection(l2)
print(ins_node.data)