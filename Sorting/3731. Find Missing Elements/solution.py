from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        lower, upper = min(nums), max(nums)
        org = set(range(lower, upper+1))

        res = set(nums) ^ org

        return sorted(list(res))


    

nums = [5,1]
print(Solution().findMissingElements(nums))