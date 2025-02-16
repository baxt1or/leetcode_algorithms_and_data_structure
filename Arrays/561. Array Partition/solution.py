from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()

        som = 0

        for i in range(0,len(nums)-1, 2):
            som+=min(nums[i], nums[i+1])

        return som

if __name__ == '__main__':

    """ Example 1: """
    nums = [6,2,6,5,1,2]
    print(Solution().arrayPairSum(nums))