from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        res = []
        
        grid = [sorted(row, reverse=True) for row in grid]

        
        for i in range(len(grid[0])):
          row = []
          for r in grid:
            row.append(r[i])
          res.append(max(row))
        return sum(res)
    

if __name__ == '__main__':
   
   """ Example 1: """
   grid = [[1,2,4],[3,3,1]]
   print(Solution().deleteGreatestValue(grid))


   """ Example 2: """
   grid = [[10]]
   print(Solution().deleteGreatestValue(grid))


   """ Example 3: """
   grid = [[35,52,74,92,25],[65,77,1,73,32],[43,68,8,100,84],[80,14,88,42,53],[98,69,64,40,60]]
   print(Solution().deleteGreatestValue(grid))