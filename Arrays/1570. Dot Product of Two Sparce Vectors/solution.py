from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        """ Takes only List of integers """
        self.nums = nums
    
    def dotProduct(self, vec: 'SparseVector') -> int:
        """ Returns the dot product of two vectors """
        result = [x*y for x, y in zip(self.nums, vec.nums)]
        return sum(result)


""" Example Use """
v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
v1.dotProduct(v2)