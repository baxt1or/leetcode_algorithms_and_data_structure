from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        

        res = []

        for c in range(len(grid[0])):
            row = []
            for r in range(len(grid)):
                row.append(len(str(grid[r][c])))
            res.append(max(row))
        
        return res

if __name__ == '__main__':

    """ Example 1: """
    grid = [[-15,1,3],[15,7,12],[5,6,-2]]
    print(Solution().findColumnWidth(grid=grid))