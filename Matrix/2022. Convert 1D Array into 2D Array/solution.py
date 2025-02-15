from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m*n != len(original):
          return []

        grid = [[0]*n for _ in range(m)]

        for i in range(m*n):
           row = i // n
           col = i % n

           grid[row][col] = original[i]
        
        return grid
    

if __name__ == '__main__':
    
    """ Example 1: """
    original = [1,2,3]
    m =1
    n =3
    print(Solution().construct2DArray(original, m, n))