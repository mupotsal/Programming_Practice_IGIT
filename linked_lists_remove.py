# learning how to remove items from a linked list
import turtle
l = turtle.Turtle()
l.fil
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_items(head):
    while head:
        print(head.data)
        head = head.next
        #head.next = None



def remove_items(head, value):
    # removing fom the middle
    prev = head
    forward = head.next
    if head.data == value:
        head.data = forward
        # head.next = None

    while forward:
        if forward.data == value:
            prev.next = forward.next
        prev = forward
        forward = forward.next

def main():
    hd = Node(6)
    a = Node(7)
    b = Node(8)
    c = Node(9)
    hd.next = a
    a.next = b
    b.next = c

    print("This is the list before renoval",print_items(hd))

    remove_items(hd,6)
    print("This is the list after removal ",print_items(hd))

main()





