def twoSum( nums, target) :
    # implement dictionaries
    # Assume the data is sorted
    my_dict = {}
    count = 0
    for i in range(len(nums)):
        if nums[i] not in my_dict.keys():
            #print(my_dict)
            my_dict[target - nums[i]] = i
        else:
            count += 1
    return count
def main():
    lis = [2,3,4,5,6,7]
    target = 9
    print(twoSum(lis,target))

main()