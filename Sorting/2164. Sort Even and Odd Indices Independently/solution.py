from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:


        odds = [nums[x] for x in range(len(nums)) if x % 2 != 0]
        evens = [nums[x] for x in range(len(nums)) if x %2 == 0]


        res = []

        odds.sort(reverse=True)
        evens.sort()
        
        i, j =0,0

        for index in range(len(nums)):
            if index %2 ==0 and i < len(nums):
                res.append(evens[i])
                i+=1
            if index % 2 != 0 and j < len(nums):
                res.append(odds[j])
                j+=1
        
        return res


if __name__ == '__main__':

    """ Example 1: """
    nums = [5,39,33,5,12,27,20,45,14,25,32,33,30,30,9,14,44,15,21]
    print(Solution().sortEvenOdd(nums))