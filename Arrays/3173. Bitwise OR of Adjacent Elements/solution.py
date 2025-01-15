from typing import List


class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        """ Stores all OR values of Adjacent elements """
        result = []

        for i in range(len(nums)-1):
            result.append(nums[i] | nums[i+1])
        return result


""" Example 1: """
nums = [1,3,7,15]
Solution().orArray(nums)

""" Example 2: """
nums = [8,4,2]
Solution().orArray(nums)

""" Example 3: """
nums = [5,4,9,11]
Solution().orArray(nums)