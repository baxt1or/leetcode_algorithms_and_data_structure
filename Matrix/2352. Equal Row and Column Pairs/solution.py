from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        cols = []

        for i in range(len(grid[0])):
          row = []
          for r in grid:
            row.append(r[i])
          cols.append(row)
      
        count = 0 

        for row in grid:
           for col in cols:
            if row == col:
              count+=1

        return count


if __name__ == '__main__':
   
   """ Example 1: """
   grid = [[3,2,1],[1,7,6],[2,7,7]]
   print(Solution().equalPairs(grid))


   """ Example 2: """
   grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
   print(Solution().equalPairs(grid))


   """ Example 3: """
   grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
   print(Solution().equalPairs(grid))