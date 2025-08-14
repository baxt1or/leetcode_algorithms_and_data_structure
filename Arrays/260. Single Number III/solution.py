from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        return [key for key, val in Counter(nums).items() if val == 1]


    
if __name__ == '__main__':
    """ Example 1: """
    nums = [1,2,1,3,2,5]
    print(Solution().singleNumber(nums))

    """ Example 2: """
    nums = [-1,0] 
    print(Solution().singleNumber(nums))