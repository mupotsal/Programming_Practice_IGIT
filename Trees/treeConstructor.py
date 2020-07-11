class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def is_empty(self):
        return len(self.items)==0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    """This file has info about how to traverse trees
    This is what is used in Depth First Search"""
    def __init__(self,root):
        self.root = Node(root)
    def preOrder(self,start):
        """R-L-R"""
        if not start:
            return
        print(start.value)
        self.preOrder(start.left)
        self.preOrder(start.right)
    def postOrder(self,start):
        if not start:
            return
        self.postOrder(start.left)
        self.postOrder(start.right)
        print(start.value)

    def levelOrder(self,start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue)>0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal


tree= BinaryTree(1) # this is the root Node
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left =Node(4)
tree.root.left.right = Node(5)
    #    1
#     2         3
# 4    5
print("PreOrder",tree.preOrder(tree.root))
print("PostOrder",tree.postOrder(tree.root))
print("LevelOrder",tree.levelOrder(tree.root))

