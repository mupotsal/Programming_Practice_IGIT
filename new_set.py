def contains_duplicate(nums):
    new_set = set() # you can declare a set by using the set constuctor method or by using the curly brackets but with at least one element
    for i in nums:
        if i not in new_set:
            new_set.add(i)
        else:
            return True
    return False

def main():
    nums = [2,3,4,5,7,8]
    print(contains_duplicate(nums))

main()