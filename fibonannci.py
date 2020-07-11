from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = [] # put open brackets
    for i, next in enumerate(text):
        print("i",i,"next",next)
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
        print("This is the stack",opening_brackets_stack)
        if next in ")]}":
            if len(opening_brackets_stack)==0:
                return "There is an error",i
            # Process closing bracket, write your code here
            check = are_matching(opening_brackets_stack[-1],next)
            if check ==0:
                return "There is a problem "
            opening_brackets_stack.pop()
    if len(opening_brackets_stack)==0:
        return "The brackets were matched correctly"
    else:
        return "There is an error"



# {,{,{
# {{{}}}

def main():
    while True:
        print("enter the text")
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
        # Printing answer, write your code here


if __name__ == "__main__":
    main()
