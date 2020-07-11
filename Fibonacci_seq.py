def Fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        print(n)
        t = Fibonacci(n-1) + Fibonacci(n-2)
        return t
def main():
    print(Fibonacci(3))

main()