from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
      
        m = len(mat)
        n = len(mat[0])

        if m*n != r *c:
          return mat
        
        grid = [[0]*c for _ in range(r)]

        for i in range(m*n):
            row = i // n
            col = i % n
            grid[i//c][i%c] = mat[row][col]
        
        return grid

if __name__ == '__main__':
    
    """ Example 1: """
    mat = [[1,2,3,4]]
    print(Solution().matrixReshape(mat=mat))