class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_reverse(self, node):
        if node is None:
            return
        self.print_reverse(node.next)
        print(node.data, end=" ")

def create_linked_list():
    linked_list = LinkedList()
    while True:
        user_input = input("Enter a number to insert into the linked list (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        linked_list.insert(int(user_input))
    return linked_list

if __name__ == "__main__":
    my_linked_list = create_linked_list()
    print("Linked list in reverse order:")
    my_linked_list.print_reverse(my_linked_list.head)

