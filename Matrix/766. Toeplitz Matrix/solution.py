from typing import List, defaultdict

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        

        grid = defaultdict(list)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                grid[r-c].append(matrix[r][c])
        
        for row in list(grid.values()):
            if len(set(row)) != 1:
                return False
        return True

if __name__ == '__main__':

    """ Example 1: """
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print(Solution().isToeplitzMatrix(matrix))