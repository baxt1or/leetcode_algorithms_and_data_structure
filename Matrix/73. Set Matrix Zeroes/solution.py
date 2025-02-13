from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[0])

        cols = set()
        rows = set()

        for r in range(n):
          for c in range(m):
            if matrix[r][c] == 0:
              rows.add(r)
              cols.add(c)

        
        for r in range(n):
            if r in rows:
              matrix[r] = [0]*m

        for c in range(m):
          if c in cols:
            for r in range(n):
              matrix[r][c] = 0
    
if __name__ == '__main__':
   
   """ Example 1: """
   matrix = [[1,1,1],[1,0,1],[1,1,1]]
   Solution().setZeroes(matrix)
   print(matrix)

   """ Example 2: """
   matrix =[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
   Solution().setZeroes(matrix)
   print(matrix)