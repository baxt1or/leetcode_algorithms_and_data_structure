from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        for i in range(len(matrix)):
          for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

        for row in matrix:
          row.reverse()

if __name__ == '__main__':
   
   """ Example 1: """
   matrix = [[1,2,3],[4,5,6],[7,8,9]]
   Solution().rotate(matrix)
   print(matrix)

   """ Example 2: """
   matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
   Solution().rotate(matrix)

