class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def breadthFirstSearch(root):
    if not root:
        return
    q = []
    q.append(root)

    while q:
        size = len(q)
        while size > 0:
            # pop the first item
            # get its children
            # then continue
            current = q.pop(0)
            print(current.val,end=' ')
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            size -= 1
        print(' ')

root = Node(1)
root.left = Node(2)
root.right= Node(3)
root.left.left=Node(4)
root.left.right = Node(5)

breadthFirstSearch(root)




