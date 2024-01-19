# ~~1. Understand how LLs are created.~~
# 2. CRUD operations
# 3. Loops in LLs
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
 
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
       
        current_node = self.head
        count = 0
        while current_node and count < position:
            current_node = current_node.next
            count += 1
        if not current_node:
            print("Error! Out of Bounds!")
            return
       
        # Logic
        new_node.next = current_node.next
        current_node.next = new_node
 
    def delete(self, value):
        current_node = self.head
 
        if current_node and current_node.data == value:
            self.head = current_node.next
            current_node = None
            return
   
        prev_node = None
        while current_node and current_node.data != value:
            prev_node = current_node
            current_node = current_node.next
       
        if current_node is None:
            print("Error! Value not found!")
            return
       
        prev_node.next = current_node.next
        current_node = None
 
    def detect_loop(self):
        slow = self.head
        fast = self.head
 
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
 
            if slow == fast:
                return True
                # If there is a loop, slow and fast will always meet
       
        return False
   
    def remove_loop(self):
        slow = self.head
        fast = self.head
 
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
 
            if (slow == fast):
                # remove the loop logic
                fast = self.head
                while fast.next != slow.next:
                    fast = fast.next
                    slow = slow.next
               
                # slow is on the node just before intersection
                slow.next = None
 
                return True
           
        return False
 
 
    def print(self):
        a = self.head
        while a:
            print(a.data, end=" ")
            a = a.next  # DO NOT FORGET TO STEP FORWARD
        print()
 
 
l = LinkedList()
for i in range(1, 7):
    l.append(i)
 
l.insert(100, 5)
l.insert(101, 0)
l.print()
