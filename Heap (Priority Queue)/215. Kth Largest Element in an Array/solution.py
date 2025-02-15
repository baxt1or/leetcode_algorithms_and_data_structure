from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        max_heap = [-x for x in nums]

        heapq.heapify(max_heap)

        
        for _ in range(k-1):
            -heapq.heappop(max_heap)
        
        return -max_heap[0]
    


if __name__ == '__main__':

    """ Example 2: """
    nums = [3,2,1,5,6,4]
    k = 2
    print(Solution().findKthLargest(nums, k))