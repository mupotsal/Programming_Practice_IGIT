def filter_odd(nums):
    required_array = []
    for i in range(len(nums)):
        if i%2 != 0:
            required_array.append(nums[i])
        return required_array

def main():
    nums = [2,4,5,6,7,8,3]
    filter_odd(nums)
    print("I expect 2,5,7,3")
main()