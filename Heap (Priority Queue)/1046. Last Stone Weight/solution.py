from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        nums = []
        for n in stones:
            heapq.heappush(nums, -n)
        

        while len(nums) > 1:
            v1 = -heapq.heappop(nums)
            v2 = -heapq.heappop(nums)
   
            if v1 == v2:
                continue
            elif v1 != v2:
                heapq.heappush(nums, -(v1-v2))
        
        return 0 if len(nums) ==0 else -nums[0]


if __name__ == '__main__':
    """ Example 1: """
    stones = [1, 3]
    print(Solution().lastStoneWeight(stones))

    """ Example 2: """
    stones = [2,7,4,1,8,1]
    print(Solution().lastStoneWeight(stones))
  