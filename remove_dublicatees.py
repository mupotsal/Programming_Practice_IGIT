def remove_dublicates(nums):
    i = 0
    for j in range(len(nums)):
        print(nums)
        if nums[i] != nums[j]:
            i = i + 1
            nums[i] = nums[j]
        print("i", i)
        print("j",j)

    print("this is", nums[:i+1])
    return nums[:i + 1]

def main():
    ls = [2,2,5,5,7,7,8]
    print(remove_dublicates(ls))
main()