from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        if mat == target:
          return True

        self.rotate(mat)
        
        if mat == target:
          return True
        
        self.rotate(mat)

        if mat == target:
          return True
        
        self.rotate(mat)

        if mat == target:
          return True
        
        return False

    def rotate(self, mat):
        n = len(mat)

        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        for row in mat:
            row.reverse()


if __name__ == '__main__':
   
   """ Example 1: """
   mat = [[0,1],[1,0]]
   target = [[1,0],[0,1]]
   print(Solution().findRotation(mat=mat, target=target))


   """ Example 2: """
   mat = [[0,1],[1,1]]
   target = [[1,0],[0,1]]
   print(Solution().findRotation(mat=mat, target=target))


   """ Example 3: """
   mat = [[0,1],[1,1]]
   target = [[1,0],[0,1]]
   print(Solution().findRotation(mat=mat, target=target))

   """ Example 4: """
   mat = [[0,0,0],[0,0,1],[0,0,1]]
   target = [[0,0,0],[0,0,1],[0,0,1]]
   print(Solution().findRotation(mat=mat, target=target))