def is_palindrome(s):
    stack = []
    for i in s:
        stack.append(i)
    print(stack)
    for i in s:
        a = stack.pop()
        print(a)
        if i!= a:
            x=2

    return 1

def main():
    word = "tomatoe"
    print(is_palindrome(word))

def palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))

def main():
    word = "axxaaxxa"
    print(palindromic(word))

main()