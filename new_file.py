def findDisappearedNumbers(nums):
    my_set = set(nums)
    print(my_set)
    lis = []
    for i in range(1, len(nums)+1 , 1):
        print(i)
        if i not in my_set:
            lis.append(i)
    return lis

def main():
    lis = [2,2,2]
    print(findDisappearedNumbers(lis))

main()