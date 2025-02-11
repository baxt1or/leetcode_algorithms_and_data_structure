from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
      
      max_val = max(max(row) for row in matrix)

      n = set(list(range(1, max_val+1)))
      
      count_col = 0
      count_row = 0

      for row in matrix:
        if n == set(row):
          count_row+=1

      res = []

      for i in range(len(matrix[0])):
        row = set()
        for r in matrix:
          row.add(r[i])
        if n == row:
          count_col+=1
           
      return count_col == count_row  == len(n)


if __name__ == "__main__":
  
  """ Example 1 """
  matrix = [[1,2,3],[3,1,2],[2,3,1]]
  print(Solution().checkValid(matrix=matrix))

  """ Example 2: """
  matrix = [[1,1,1],[1,2,3],[1,2,3]]
  print(Solution().checkValid(matrix=matrix))