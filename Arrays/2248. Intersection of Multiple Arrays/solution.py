from collections import Counter
from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        n = len(nums)

        res = []

        for num in nums:
            res.extend(num)
        
        return sorted([key for key, val in Counter(res).items() if val == len(nums)])


if __name__ == '__main__':

    """ Example 1: """
    nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
    print(Solution().intersection(nums))