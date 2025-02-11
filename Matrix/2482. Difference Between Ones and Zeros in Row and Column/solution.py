from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_row = []
        ones_col = []


        for i in range(len(grid)):
          count = 0
   
          for j in range(len(grid[i])):
            if grid[i][j] == 1:
              count+=1
          ones_row.append(count)
        
        for i in range(len(grid[0])):
            count = 0
            for row in grid:
                if row[i] == 1:
                    count+=1
            ones_col.append(count)
            
         
        diff = []
        
        for i in range(len(grid)):
          row = []

          for j in range(len(grid[0])):
            res = ones_row[i] + ones_col[j] - (len(ones_row) - ones_row[i])  - (len(ones_col) - ones_col[j])
            row.append(res)
          diff.append(row)

        return diff
    
if __name__ == "__main__":
   """ Example 1: """
   grid = [[0,1,1],[1,0,1],[0,0,1]]
   print(Solution().onesMinusZeros(grid=grid))

   """ Example 2: """
   grid = [[1,1,1],[1,1,1]]
   print(Solution().onesMinusZeros(grid=grid))