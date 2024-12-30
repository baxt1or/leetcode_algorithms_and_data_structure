from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        """ Returns distinct k of 1's in their binary representation  """
        som = 0       
        bins =  [bin(i) for i in range(len(nums))]

        for i in range(len(bins)):
            if bins[i].count('1') == k:
                som+=nums[i]
        return som
            
""" Example 1:  """
nums = [5,10,1,5,2]
k = 1
Solution().sumIndicesWithKSetBits(nums, k)


""" Example 2: """
nums = [4,3,2,1]
k = 2
Solution().sumIndicesWithKSetBits(nums, k)