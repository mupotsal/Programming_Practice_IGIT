import random
from datetime import datetime


def mergesort(A):
    n = len(A)
    if n > 1:
        mid = n // 2
        B = A[0:n // 2]
        C = A[n // 2:n]
        mergesort(B)
        mergesort(C)
        merge(B, C, A)


def merge(B, C, A):
    bIndex = cIndex = 0
    m1 = len(B)
    m2 = len(C)
    n = len(A)
    i = 0
    while (bIndex < m1) and (cIndex < m2):
        small = B[bIndex]
        if C[cIndex] < small:
            small = C[cIndex]
            cIndex += 1
        else:
            bIndex += 1
        A[i] = small
        i += 1
    while bIndex < m1:
        A[i] = B[bIndex]
        bIndex += 1
        i += 1
    while cIndex < m2:
        A[i] = C[cIndex]
        cIndex += 1
        i += 1

def quicksort(A):
    n = len(A)
    A.append(1E30)
    quicksortAux(A, 0, n - 1)
    del A[n]


def quicksortAux(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quicksortAux(A, l, s - 1)
        quicksortAux(A, s + 1, r)


def partition(A, l, r):
    p = A[l]
    i = l
    j = r + 1
    stillLooping = True
    while stillLooping:
        sL = True
        while sL:
            i = i + 1
            if A[i] >= p: sL = False
        sL = True
        while sL:
            j = j - 1
            if A[j] <= p: sL = False
        A[i], A[j] = A[j], A[i]
        if i >= j: stillLooping = False
    A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def rand_func():
    store_arr=[]
    ran = random.Random()
    n = ran.randint(1000,5000)
    for i in range(n):
        value = ran.randint(0,400)
        store_arr.append(value)
    return store_arr

def main():
    outfile = open("data.txt","w")
    for i in range(100):
        A=rand_func()
        n=len(A)
        Aoriginal = A[0:n]
        before=datetime.now()
        mergesort(A)
        after=datetime.now()
        elapsed=after-before
        ms_microseconds=elapsed.total_seconds()*(10**6)
        A=Aoriginal[0:n]
        before = datetime.now()
        quicksort(A)
        after=datetime.now()
        elapsed=after-before
        qs_microseconds = elapsed.total_seconds() * (10 ** 6)
        outfile.write(str(n)+"\t"+str(ms_microseconds)+"\t"+str(qs_microseconds)+"\n")

        print(str(n)+"\t"+str(ms_microseconds)+"\t"+str(qs_microseconds))



main()


