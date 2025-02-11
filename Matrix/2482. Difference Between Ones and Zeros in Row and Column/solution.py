from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        ones_row = [sum(row) for row in grid]
        ones_col = [sum(grid[row][col] for row in range(len(grid))) for col in range(len(grid[0]))]
        
    
        for i in range(len(grid)):
          for j in range(len(grid[0])):
            grid[i][j] = ones_row[i] + ones_col[j] - (len(ones_row) - ones_row[i])  - (len(ones_col) - ones_col[j])
        return grid
    
if __name__ == "__main__":
   """ Example 1: """
   grid = [[0,1,1],[1,0,1],[0,0,1]]
   print(Solution().onesMinusZeros(grid=grid))

   """ Example 2: """
   grid = [[1,1,1],[1,1,1]]
   print(Solution().onesMinusZeros(grid=grid))