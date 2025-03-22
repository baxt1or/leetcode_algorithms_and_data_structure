from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        duplicates = set()

        for num in nums:
            if num in duplicates:
                return True
            duplicates.add(num)
        
        return False
        



if __name__ == '__main__':

    """ Example 1: """
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums=nums))
