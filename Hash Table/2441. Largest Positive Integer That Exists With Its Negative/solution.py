from typing import List
from collections import Counter

class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        count = Counter(nums)

        res = []

        for n in nums:
            if n in count and -n in count:
                res.append(n)
        
        return -1 if not res else max(res)
    

if __name__ == '__main__':
    """ Example 1: """
    nums = [-9,-43,24,-23,-16,-30,-38,-30]
    print(Solution().findMaxK(nums))