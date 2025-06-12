from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        n = len(nums)

        r = abs(nums[0] - nums[-1])

        max_element = 0

        for i in range(0, n-1):
            max_element = max(max_element, abs(nums[i] - nums[i+1]))

        return r, max_element


if __name__ == '__main__':

    """ Example 1: """
    nums = [-4,-2,-3]
    print(Solution().maxAdjacentDistance(nums=nums))


    """ Example 2: """
    nums = [5, 5]
    print(Solution().maxAdjacentDistance(nums=nums))