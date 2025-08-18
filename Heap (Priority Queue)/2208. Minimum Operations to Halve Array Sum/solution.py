import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        total = sum(nums) / 2

        arr = []

        for n in nums:
            heapq.heappush(arr, -n)
        
        ttl = sum(nums)
        i = 0

        while ttl > total/2:
            v = -heapq.heappop(arr)
            r = v/2
            heapq.heappush(arr, -r)
            ttl -=v/2
            i+=1

            if ttl <= total:
                return i
            else:
                continue
        
        return i


if __name__ == '__main__':
    """ Example 1: """
    nums = [5,19,8,1]
    print(Solution().halveArray(nums))