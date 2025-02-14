from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:

      nums = sorted(nums)

      max_pair = 0
      
      i = 0
      j = len(nums) -1

      while i <= j:

        val = nums[i]+nums[j]
        max_pair = max(max_pair, val)
        i+=1
        j-=1
      
      return max_pair
    

if __name__ == '__main__':
   
   """ Example 1: """
   nums = [3,5,2,3]
   print(Solution().minPairSum(nums=nums))


   """ Example 2: """
   nums = [3,5,4,2,4,6]
   print(Solution().minPairSum(nums=nums))