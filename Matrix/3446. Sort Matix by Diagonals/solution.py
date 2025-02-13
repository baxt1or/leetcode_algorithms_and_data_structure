from typing import List, defaultdict 

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])

        result = defaultdict(list)

        for r in range(n):
          for c in range(m):
            result[r-c].append(grid[r][c])
        
        
        for key in result:
          if key < 0:
             result[key].sort()
          else:
            result[key].sort(reverse=True)
        
        
        for r in range(n):
          for c in range(m):
            grid[r][c] = result[r-c].pop(0)
        
        return grid
    
if __name__ == '__main__':
   
   """ Example 1: """
   grid = [[1,7,3],[9,8,2],[4,5,6]]
   print(Solution().sortMatrix(grid))


   """ Example 2: """
   grid = [[0,1],[1,2]]
   print(Solution().sortMatrix(grid))