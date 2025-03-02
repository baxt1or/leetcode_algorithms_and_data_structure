from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        def move_zeros(nums):

            for n in nums:
                if n == 0:
                    nums.remove(n)
                    nums.append(0)

        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        
        move_zeros(nums=nums)

        return nums

if __name__ == '__main__':

    """ Example 1: """
    nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
    print(Solution().applyOperations(nums=nums))