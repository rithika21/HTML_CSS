# ~~1.UNDERSTAND  HOW LLPS ARE CREATED~``
# 2.CRUD OPERATIONS
# 3.LOOP IN LLS
# 4.SORT THE LLS(MERGE SORT)
# 5.INTERSECTION IN LLS
# 6.SOME INTERSECTING PROBLEMS


# RECALL : EVERY CLASS : DATA +  FUNCTIONS

class Node:
    # DATA 
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_List:
    #data
    def __init__(self):
        self.head = None   
    #function
    def append(self,data):
        new_node = Node(data)
        #if my head is empty
        if self.head is None:
            self.head = new_node
            return
        #if head is not empty
        last_node = self.head
        while last_node.next: 
            last_node=last_node.next
        last_node.next=new_node
    def print(self):
        a=self.head
        while a:
            print(a.data,end=" ")
            a=a.next
            #print()                     
   

l=Linked_List()
for i in range(1,101):
    l.append(i)
l.print()



#   https://pastebin.com/iZd2QJQV