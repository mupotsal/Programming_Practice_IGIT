def push_zeros(nums): # space saved
    i = 0
    for j in range(1, len(nums), 1):
        if j < len(nums):
            print("i", i)
            print("j", j)
            if nums[i] == 0 and nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
            elif nums[i] != 0 and nums[j] == 0:
                i +=1
            elif nums[i] != 0 and nums[j] != 0:
                i+=1
        print(nums)
    return nums


def push_zero_another_list(nums):
    # create a new list
    nums1 = []
    for i in range(len(nums)):
        if nums[i]!=0:
            nums1.append(nums[i])

    for i in range(len(nums)):
        if nums[i] ==0:
            nums1.append(0)
    print(nums1)
    return nums1

def main():
    nums = [4,2,4,0,0,3,0,5,1,0]
    print(push_zero_another_list(nums))

main()