from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        res = []

        for n in nums:
            heapq.heappush(res, -n)
                
        ans = []
        i = 0

        while i != k:
            val = -heapq.heappop(res)
            ans.append(val)
            i+=1
        
        return ans[-1]


if __name__ == '__main__':
    """ Example 1: """
    nums = [3,2,1,5,6,4]
    k = 2
    print(Solution().findKthLargest(nums, k))


    """ Example 2: """
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(Solution().findKthLargest(nums, k))