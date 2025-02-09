from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def dotProduct(self, vec) -> int:
        result = 0

        for i in range(len(vec.nums)):
            result += (self.nums[i] * vec.nums[i])
        return result


""" Example Use """
v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
v1.dotProduct(v2)