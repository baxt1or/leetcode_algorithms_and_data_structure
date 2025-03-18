from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        count = {}

        for n in nums:
            count[n] = count.get(n, 0)+1
        
        
        for key, val in count.items():
            if val % 2 != 0:
                return False
        return True


if __name__ == '__main__':

    """ Example 1: """
    nums = [3,2,3,2,2,2]
    print(Solution().divideArray(nums=nums))


    """ Example 2: """
    nums = [1,2,3,4]
    print(Solution().divideArray(nums=nums))