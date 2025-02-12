from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        ans : List[int] = []

        for i in range(len(matrix[0])):
            row_data : List[int]= []

            for row in matrix:
                row_data.append(row[i])
            ans.append(row_data)
        return ans