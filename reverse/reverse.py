class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if (node is None):
            return None
        if node.next_node is None:
            return node 
        prev = None
        node = self.head
        while node:
            next=node.next_node 
            node.next_node = prev
            prev=node
            node = next
        self.head = prev


        #     def reverse_list(self, head):
        #   if head is None or head.next_node is None:
        #     return head
        # new_head = reverse_List(head.next_node)
        # head.next_node.next_node = head
        # head.next_node = None
        # return new_head
        
         



