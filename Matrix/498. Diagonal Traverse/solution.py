from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        n = len(mat)
        m = len(mat[0])

        ans = []
    
        res = [[] for _ in range(n+m-1)]
        
        for i in range(n):
          for j in range(m):
            res[i+j].append(mat[i][j])
        
       
        for i in range(len(res)):
          if i % 2 == 0:
             ans.extend(reversed(res[i]))
          else:
               ans.extend(res[i])
        return ans


if __name__ == '__main__':
   
   """ Example 1: """
   mat = [[2,5],[8,4],[0,-1]]
   print(Solution().findDiagonalOrder(mat))