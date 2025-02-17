import math
from typing import List

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        max_distance = 0

        def prime(n):
            if n < 2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        i,j=0,1

        
        while i < len(nums) and j < len(nums):

            if prime(nums[j]):
                if prime(nums[i]):
                    max_distance = max(max_distance, j-i)
                else:
                    i = j
            j+=1
        
        return max_distance

nums = [4,2,9,5,3]
print(Solution().maximumPrimeDifference(nums=nums))