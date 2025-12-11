
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def recursive_sum(self):
        def sum_helper(node):
            if node is None:
                return 0
            return node.data + sum_helper(node.next)
        return sum_helper(self.head)

    def recursive_reverse(self):
        def reverse_helper(prev, current):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return reverse_helper(current, next_node)
        self.head = reverse_helper(None, self.head)

    def recursive_search(self, target):
        def search_helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return search_helper(node.next)
        return search_helper(self.head)
        """
        TODO:
        - Return True if 'target' is found, otherwise False, using recursion.
        - Consider a helper function that:
          1. Returns False if the current node is None.
          2. Returns True if current node's data == target.
          3. Otherwise, recurse on the next node.
        """
        pass

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
