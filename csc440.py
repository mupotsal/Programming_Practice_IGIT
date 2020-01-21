import random
from datetime import datetime


def bubblesort(arr):
    for i in range(len(arr)-2):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1] = temp
    return arr


def rand_func():
    store_arr = []
    ran = random.Random()
    n = ran.randint(1000,5000)
    for i in range(n):
        value = ran.randint(0,400)
        store_arr.append(value)
    return store_arr

def main():
    for i in range(100):
        outfile = open("data.txt", "w")
        rand_nums = (rand_func())
       # print(rand_nums)
        before = datetime.now()
        bubblesort(rand_nums)
        after = datetime.now()
        elapsed = after - before
        microseconds = elapsed.total_seconds()*(10**6)
        print(str(len(rand_nums))+"\t"+str(microseconds))

main()
