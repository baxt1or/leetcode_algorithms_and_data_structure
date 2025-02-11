from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_val = nums[0]

        for num in nums:
            if num < min_val:
                min_val = num
        return min_val
    

if __name__ == "__main__":
    
    """ Example 1: """
    nums = [1, 3, 5]
    print(Solution().findMin(nums=nums))

    """ Example 2: """
    nums = [2,2,2,0,1]
    print(Solution().findMin(nums=nums))