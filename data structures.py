#singly linked list
# steps 
    # create node
    # list

class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None

node1 =Node(10)
node2 =Node(20)
node3 =Node(30)

class LinkedList:
    def __init__(self):
        self.head =None
        self.tail=None
    
    def add_node_at_first_position(self,node):
        self.head = node
    
    def print_list(self):
        node=self.head
        while node!=None:
            print(node.data)
            node=node.ref

linked_list=LinkedList()
linked_list.add_node_at_first_position(node1)
linked_list.add_node_at_first_position(node2)
linked_list.add_node_at_first_position(node3)
linked_list.print_list()