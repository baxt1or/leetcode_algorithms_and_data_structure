from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        nums.sort()

        return nums
    

if __name__ == '__main__':
    
    """ Example 1: """
    nums = [4,3,2,1]
    print(Solution().transformArray(nums))