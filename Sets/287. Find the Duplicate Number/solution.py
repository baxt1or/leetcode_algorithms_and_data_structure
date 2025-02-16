from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        res = []
        seen = set()

        for n in nums:
            if n in seen:
                res.append(n)
            seen.add(n)
        
        return res[0] if res else -1

if __name__ == "__main__":

    """ Example 1: """
    nums = [1,3,4,2,2]
    print(Solution().findDuplicate(nums))