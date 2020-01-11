# Given an array search for a given item

def whl_linear_search(alist, x):
    i = 0
    while i < len(alist):
        if alist[i] == x:
            return i
        else:
            i += 1
    return -1


def fo_linear_search(alist, x):
    for i in range(len(alist)):
        if alist[i] == x:
            return i
    return -1


def rec_linear_search(alist, i, x):
    if i == len(alist):
        return -1
    if alist[i] == x:
        return i
    return (rec_linear_search(alist, i + 1, x))


def main():
    alist = [2, 4, 3, 6, 7,5, 1, 2,9]
    x = 6
    print(whl_linear_search(alist, x))
    print(fo_linear_search(alist, x))
    print(rec_linear_search(alist, 0, x))


main()
