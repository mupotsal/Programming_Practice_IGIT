class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # lis = []    #This is the method to solve it wthout usung sets
        # for i in nums:
        #     if i in lis:
        #         return i
        #     else:
        #         lis.append(i)

        my_other_set = {}
        for i in nums:
            if i not in my_other_set:
                my_other_set[i] = i
            else:
                return i