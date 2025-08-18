import heapq
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        res = []

        for n in nums:
            heapq.heappush(res, n)

        
        ans = []

        for _ in range(len(nums)):
            val = heapq.heappop(res)
            ans.append(val)
        
        return ans
    

if __name__ == '__main__':
    """ Example 1: """
    nums = [5,1,1,2,0,0]
    print(Solution().sortArray(nums))