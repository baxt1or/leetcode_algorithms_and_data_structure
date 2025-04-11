from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)
        dict_nums = {}

        res = []

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dict_nums:
                dict_nums[sorted_nums[i]] = i

    
        for num in nums:
            res.append(dict_nums[num])

        return res


if __name__ == '__main__':

    """ Exampl 1: """
    nums = [8,1,2,2,3]
    print(Solution().smallerNumbersThanCurrent(nums))