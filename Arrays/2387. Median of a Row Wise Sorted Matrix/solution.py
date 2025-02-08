from typing import List

class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:

        nums = self.flatten(grid)

        n = len(nums)

        mid = n //2

        if n % 2 != 0:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid-1]) / 2
    
    def flatten(self, mat):

        arr = []

        for row in mat:
            if isinstance(row, list):
                arr.extend(self.flatten(row))
            else:
                arr.append(row)
        return sorted(arr)