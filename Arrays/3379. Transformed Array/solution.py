from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        n = len(nums)

        res = [0]*n

        for i in range(n):
            if nums[i] > 0:
                idx = (i+ nums[i]) % n
                res[i] = nums[idx]
            if nums[i] < 0:
                idx = (i - abs(nums[i])) % n
                res[i] = nums[idx]
            if nums[i] ==0:
                res[i] = nums[i]
        
        return res

if __name__ == '__main__':

    """ Example 1: """
    nums = [3,-2,1,1]
    print(Solution().constructTransformedArray(nums))