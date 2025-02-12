from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        non = []
        res = []
        n = len(grid)

        for i in range(n):
          for j in range(n):
            if i == j or i == n -1 -j:
              res.append(grid[i][j])
            else:
              non.append(grid[i][j])
        
        count_non = 0
        count_res = 0

        for n in res:
          if n == 0:
            count_res +=1
        
        for n in non:
          if n != 0:
            count_non +=1
        
        return count_non == 0 and count_res == 0
    
if __name__ == "__main__":
  
    """ Example 1: """
    grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
    print(Solution().checkXMatrix(grid))

    """ Example 2: """
    grid = [[5,7,0],[0,3,1],[0,5,0]]
    print(Solution().checkXMatrix(grid))