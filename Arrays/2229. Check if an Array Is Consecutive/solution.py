from typing import List

class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        
        n = len(nums)
        min_val = min(nums)

        return set([x for x in range(min_val, (min_val+n-1)+1)]) == set(nums)

if __name__ == '__main__':

    """ Example 1: """
    nums = nums = [1,3,4,2]
    print(Solution().isConsecutive(nums))