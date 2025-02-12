from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        res = []
        ans = []

        for i in range(len(mat)):
          r = mat[i].count(1)
          if r != 0:
             res.append([i,r])

        return max(res, key=lambda item:item[1]) if res else [0,0]
    

if __name__ == '__main__':
   
   """ Example 1: """
   mat = [[0,1],[1,0]]
   print(Solution().rowAndMaximumOnes(mat))


   """ Example 2: """
   mat =[[0,0,0],[0,1,1]]
   print(Solution().rowAndMaximumOnes(mat))


   """ Example 3: """
   mat = [[0,0],[1,1],[0,0]]
   print(Solution().rowAndMaximumOnes(mat))


   """ Example 4: """
   mat = [[0,1],[1,1]]
   print(Solution().rowAndMaximumOnes(mat))


   """ Example 5: """
   mat = [[0],[0]]
   print(Solution().rowAndMaximumOnes(mat=mat))