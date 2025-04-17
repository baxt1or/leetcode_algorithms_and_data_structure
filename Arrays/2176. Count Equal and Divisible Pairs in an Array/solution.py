from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        n = len(nums)
        count = 0
    
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    count+=1
        return count
        


if __name__ == '__main__':

    """ Example 1: """

    nums = [3,1,2,2,2,1,3]
    k = 2
    print(Solution().countPairs(nums, k))