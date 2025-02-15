from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        nums.sort(reverse=True)

        count = {}

        for n in nums:
          count[n] = count.get(n, 0)+1
        
        res = [key for key, val in count.items() if val == 1]

        return res[0] if res else -1


if __name__ == '__main__':
    
    """ Example 1: """
    nums = [5,7,3,9,4,9,8,3,1]
    print(Solution().largestUniqueNumber(nums))