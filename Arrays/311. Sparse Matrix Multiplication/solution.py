from typing import List
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        ans = []
        
        mat = self.transpose(mat2)

        for a in mat1:
            row = []
            for b in mat:
                row.append(self.dot_product(a, b))
            ans.append(row)
        return ans

    def transpose(self, mat):
        ans = []

        for i in range(len(mat[0])):
            row_data = []
            for row in mat:
                row_data.append(row[i])
            ans.append(row_data)
        return ans
    
    def dot_product(self, arr1, arr2):
        return sum([x*y for x, y in zip(arr1, arr2)])