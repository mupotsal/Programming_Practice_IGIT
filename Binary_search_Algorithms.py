def whi_binary_search(alist,x):
    """
     # the following code if for Binary search using the while loop
    #always  test ofor the end cases/
    :param alist:
    :param x:
    :return:
    """

    l = 0
    r = len(alist)

    while l<r:
        mid_val = (l + r) // 2
        if alist[mid_val]==x:
            return mid_val
        elif alist[mid_val]<x:
            l = mid_val +1
        else:
            r = mid_val -1

    return -1

def rec_binary_search(alist,x,l,r):
    mid_val = (l+r)//2
    if l>r:
        return -1
    if alist[mid_val]==x:
        return mid_val

    if alist[mid_val]<x:
        return rec_binary_search(alist,x,mid_val+1,r)
    else:
        return rec_binary_search(alist, x, l, mid_val -1)





def main():
    alist =[1,2,3,4,5,6,7,8,9,10]
    x =6
    r = len(alist)
    print(whi_binary_search(alist,x))
    print(rec_binary_search(alist,x,0,r))


main()

