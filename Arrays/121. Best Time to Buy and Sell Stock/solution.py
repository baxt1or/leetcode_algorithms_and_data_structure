from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
      min_price = float('inf')
      max_profit = 0

      for price in prices:

        if price < min_price:
          min_price = price
        
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
      return max_profit

if __name__ == '__main__':
   
   """ Example 1: """
   prices = [7,1,5,3,6,4]
   print(Solution().maxProfit(prices))

   """ Example 2: """
   prices = [7,6,4,3,1]
   print(Solution().maxProfit(prices))