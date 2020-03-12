class Node():
    def  __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

class Binary_Tree():
    def __init__(self,root):
        self.root = Node(root)

    def preorder_print(self,root):

        if root:
            print(root.value)
            self.preorder_print(root.left)
            self.preorder_print(root.right)

    def postorder_print(self,start):
        if start:
            self.postorder_print(start.left)
            self.postorder_print(start.right)
            print(start.value)



tree = Binary_Tree(1) # declaring a Binary tree with a 1 being the root
tree.root.left = Node(2) # this is the left child of the root node
tree.root.right = Node(3) # this is the right child of the root node
tree.root.left.left = Node(4)

tree.preorder_print(tree.root)
print("The following is the post-order print")
tree.postorder_print(tree.root)
