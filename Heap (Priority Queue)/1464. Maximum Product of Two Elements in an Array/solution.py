from typing import List
import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        arr = []

        for n in nums:
            heapq.heappush(arr, -n)
        
        ans = 0

        for _ in range(1):
            v1 = -heapq.heappop(arr)
            v2 = -heapq.heappop(arr)

            ans = (v1-1) * (v2-1)
        
        return ans
    

if __name__ == '__main__':
    """ Example 1: """
    nums = [3,4,5,2]
    print(Solution().maxProduct(nums))