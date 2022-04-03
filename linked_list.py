class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        node = Node(data)

        if self.head == None:
            self.head = node
        
        else:
            temp = self.head
            while temp.next != None:
                temp=temp.next

            temp.next = node
    
    def print(self):

        temp = self.head

        while temp != None:
            print(temp.data, end=" -> ")
            temp= temp.next
        print()

linked_list = LinkedList()
print("Linked List")
while True:
    print("Operations:")
    print("\t 1 to Append")
    print("\t 2 to Print")

    operation = int(input("Enter Operation Code: "))

    if operation == 1:
        linked_list.append(int(input("Enter data: ")))
    elif operation == 2:
        linked_list.print()
    else:
        print("Invalid operation")
