from typing import List, defaultdict 

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        n = len(mat)
        m = len(mat[0])

        res = defaultdict(list)

        for r in range(n):
          for c in range(m):
            res[r-c].append(mat[r][c])

        
        for key in res:
          res[key].sort(reverse=True)
        
        for r in range(n):
          for c in range(m):
            mat[r][c] = res[r-c].pop()
        
        return mat
    
if __name__ == '__main__':
   
   """ Example 1: """
   mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
   print(Solution().diagonalSort(mat))


   """ Example 2: """
   mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
   print(Solution().diagonalSort(mat))