from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        max_value = 0

        for i in range(len(colors)):
          for j in range(i+1,len(colors)):
              if colors[i] != colors[j]:
                val = abs(i-j)
                max_value = max(max_value, val)      
        return max_value

if __name__ == '__main__':
   
   """ Example 1: """
   colors = [1,1,1,6,1,1,1]
   print(Solution().maxDistance(colors=colors))


   """ Example 2: """
   colors = [1,8,3,8,3]
   print(Solution().maxDistance(colors=colors))


   """ Example 3: """
   colors = [0,1]
   print(Solution().maxDistance(colors=colors))