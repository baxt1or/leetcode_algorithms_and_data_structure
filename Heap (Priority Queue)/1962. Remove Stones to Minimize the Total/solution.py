import math
from typing import List
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        nums = []
        for p in piles:
            heapq.heappush(nums, -p)
        

        for _ in range(k):
            v = -heapq.heappop(nums)
            p = math.floor(v/2+ 0.5)
            heapq.heappush(nums, -p)
        
        return sum([abs(x) for x in nums])
    

if __name__ == '__main__':
    """ Example 1: """
    piles = [5,4,9]
    k = 2
    print(Solution().minStoneSum(piles, k))


    """ Example 2: """
    piles = [1]
    k = 100000
    print(Solution().minStoneSum(piles, k))