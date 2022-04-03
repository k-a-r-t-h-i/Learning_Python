from numpy import inner, trim_zeros


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def add(self,data):
        node = Node(data)

        if self.root == None:
            self.root = node
        
        else:
            def add_leaf(self, data, root):
                inner_temp = root
                if data < inner_temp.data:
                    if inner_temp.left == None:
                        inner_temp.left = node
                    else:
                        add_leaf(self, data, inner_temp.left)
            
                if data > inner_temp.data:
                    if inner_temp.right == None:
                        inner_temp.right = node
                    else:
                        add_leaf(self, data, inner_temp.right)

            add_leaf(self, data, self.root)
    
    def inorder(self):

        if self.root == None:
            print("Tree is Empty!!")
            return

        def print_leaf(self, root):
            inner_temp = root

            #left
            if inner_temp.left != None:
                print_leaf(self, inner_temp.left)

            #root
            print(inner_temp.data, end=" -> ")

            #right
            if inner_temp.right != None:
                print_leaf(self, inner_temp.right)

        print_leaf(self, self.root)
        print()

    def preorder(self):

        if self.root == None:
            print("Tree is Empty!!")
            return

        def print_leaf(self, root):
            inner_temp = root

            #root
            print(inner_temp.data, end=" -> ")
            
            #left
            if inner_temp.left != None:
                print_leaf(self, inner_temp.left)

            #right
            if inner_temp.right != None:
                print_leaf(self, inner_temp.right)

        print_leaf(self, self.root)
        print()

    def postorder(self):

        if self.root == None:
            print("Tree is Empty!!")
            return

        def print_leaf(self, root):
            inner_temp = root

            #left
            if inner_temp.left != None:
                print_leaf(self, inner_temp.left)

            #right
            if inner_temp.right != None:
                print_leaf(self, inner_temp.right)

            #root
            print(inner_temp.data, end=" -> ")

        print_leaf(self, self.root)
        print()

bst = BinarySearchTree()
print("Binary Search Tree")
while True:
    print("Operations:")
    print("\t 1 to Add")
    print("\t 2 to Inorder")
    print("\t 3 to Inorder")
    print("\t 4 to Inorder")

    operation = int(input("Enter Operation Code: "))

    if operation == 1:
        bst.add(int(input("Enter data: ")))
    elif operation == 2:
        bst.inorder()
    elif operation == 3:
        bst.preorder()
    elif operation == 4:
        bst.postorder()
    else:
        print("Invalid operation")
