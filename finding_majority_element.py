def majorityElement( nums) :
    my_dict = {}

    for i in range(len(nums)):
        if nums[i] not in my_dict.keys():
            # print(my_dict)
            my_dict[nums[i]] = 1
        else:
            my_dict[nums[i]] += 1
    maj_num = len(nums) / 2
    for key, value in my_dict.items():
        if value > maj_num:
            return key