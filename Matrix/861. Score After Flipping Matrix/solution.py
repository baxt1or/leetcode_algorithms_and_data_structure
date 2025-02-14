from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        for r in range(n):
          if grid[r][0] == 0:
            for c in range(m):
              grid[r][c] = 1- grid[r][c]
        
      
        
        for c in range(m):
          col = [grid[r][c] for r in range(n)]

          if col.count(0) > col.count(1):
            for r in range(n):
              grid[r][c] = 1 - grid[r][c]
      
        som = 0


        for row in grid:
          val = int("".join([str(x) for x in row]), 2)
          som+=val 
        
        return som
    
if __name__ == '__main__':
  
    """ Example 1: """
    grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(Solution().matrixScore(grid))


    """ Example 2: """
    grid  = [[0,1],[0,0]]
    print(Solution().matrixScore(grid))


    """ Example 3: """
    grid = [[0]]
    print(Solution().matrixScore(grid))