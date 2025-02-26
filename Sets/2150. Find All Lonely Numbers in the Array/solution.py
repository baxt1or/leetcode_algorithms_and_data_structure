from collections import Counter
from typing import List

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:

        unique_nums = set([key for key, val in Counter(nums).items() if val == 1])

        ns = set(nums)
        
        res = []

        for n in nums:
            if n in unique_nums and n+1 not in ns and n-1 not in ns:
                res.append(n)
        
        return res
        

if __name__ == '__main__':
    
    """ Example 1: """
    nums = [1,3,5,3]
    print(Solution().findLonely(nums))