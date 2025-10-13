from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
 
        n = len(nums)

        res = [0]*n

        left = [0]*n
        left[0] = nums[0]

        right = [0]*n
        
        right[n-1] = nums[n-1]

        for i in range(1,n):
            left[i] = left[i-1] * nums[i]

        for i in range(n-2, -1,-1):
            right[i] = right[i+1] * nums[i]
        
        for i in range(n):

            if i == 0:
                res[i] = right[1]
            elif i == n-1:
                res[i] = left[n-2]
            else:
                res[i] = left[i-1]*right[i+1]
        
        return res
    

if __name__ == '__main__':
    """ Example 1: """
    nums = [4,3,2,1,2]
    res = Solution().productExceptSelf(nums)

    assert res == [12,16,24,48,24]
