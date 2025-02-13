from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        max_profit = 0 
        min_price = float('inf')
    
        for n in nums:

          if n < min_price:
            min_price = n
          
          profit = n - min_price
          max_profit = max(max_profit, profit)

        return -1 if max_profit == 0 else max_profit

if __name__ == '__main__':
   
   """ Example 1: """
   nums = [7,1,5,4]
   print(Solution().maximumDifference(nums=nums))


   """ Example 2: """
   nums = [9,4,3,2]
   print(Solution().maximumDifference(nums=nums))


   """ Example 3: """
   nums = [1,5,2,10]
   print(Solution().maximumDifference(nums=nums))