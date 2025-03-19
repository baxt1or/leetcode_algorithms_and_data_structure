from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(len(nums)):
            result = len(set(nums[:i])) - len(set(nums[i:]))
            res.append(result)

        
        n = abs(res[0])

        res.append(n)

        return res[1:]
    

if __name__ == '__main__':

    """ Example 1: """
    nums = [3,2,3,4,2]
    print(Solution().distinctDifferenceArray(nums))

    """ Example 2: """
    nums = [1,2,3,4,5]
    print(Solution().distinctDifferenceArray(nums))