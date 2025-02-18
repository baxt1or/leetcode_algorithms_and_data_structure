from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        n = len(nums)

        res = []

        odds = [nums[i] for i in range(n) if nums[i] %2 != 0]
        evens = [nums[i] for i in range(n) if nums[i] % 2 == 0]

        i, j = 0, 0

        for idx in range(n):
            if idx % 2 != 0 and i < len(odds):
                res.append(odds[i])
                i+=1
            if idx % 2 ==0 and j < len(evens):
                res.append(evens[j])
                j+=1
        
        return res

if __name__ == '__main__':

    """ Example 1: """
    nums = [4,2,5,7]
    print(Solution().sortArrayByParityII(nums))