from typing import List

class Solution:
    def transpose(self, matrix):
   
      m = len(matrix)
      n = len(matrix[0])
      transposed = [[0] * m for _ in range(n)]

      for i in range(m):
        for j in range(n):
          transposed[j][i] = matrix[i][j]
      
      return transposed
        
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        matrix = self.transpose(matrix)
        
        for row in matrix:
          max_val = max(row)
          for i in range(len(row)):
            if row[i] == -1:
              row[i] = max_val
        

        matrix = self.transpose(matrix)

        return matrix


if __name__ == '__main__':
   
   """ Example 1: """
   matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
   print(Solution().modifiedMatrix(matrix))

   """ Example 2: """
   matrix = [[2,-1,2,-1,2],[1,0,-1,2,-1],[2,-1,-1,-1,2],[2,1,2,-1,2],[0,1,0,0,0],[0,0,0,0,-1],[2,-1,2,2,0],[0,1,0,2,2],[2,2,0,1,-1]]
   print(Solution().modifiedMatrix(matrix))