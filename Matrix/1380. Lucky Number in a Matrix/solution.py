from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        rows = [min(row) for row in matrix]

        cols = []

        for i in range(len(matrix[0])):
            row = []
            for r in matrix:
                row.append(r[i])
            cols.append(max(row))
        return list(set(rows).intersection(set(cols)))

if __name__ == "__main__":
    """ Example 1: """
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    print(Solution().luckyNumbers(matrix))

    """ Example 2: """
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    print(Solution().luckyNumbers(matrix))