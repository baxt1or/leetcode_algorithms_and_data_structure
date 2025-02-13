from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

      max_profit = 0
      
      for i in range(1, len(prices)):

        if prices[i] > prices[i-1]:
          profit = prices[i] - prices[i-1]
          max_profit += profit
      return max_profit


if __name__ == '__main__':
   
   """ Example 1: """
   prices = [7,1,5,3,6,4]
   print(Solution().maxProfit(prices))


   """ Example 2: """
   prices = [1,2,3,4,5]
   print(Solution().maxProfit(prices))


   """ Example 3: """
   prices = [7,6,4,3,1]
   print(Solution().maxProfit(prices))